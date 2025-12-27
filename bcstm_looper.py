"""
BCSTM Looper Script
===================
A quick way to loop 3DS BCSTM audio files without using external libraries 
by hex-editing the values found in the "Stream Info" block.

For more information on the file structure, read here: 
https://www.3dbrew.org/w/index.php?title=BCSTM

DISCLOSURE: Majority of the code was generated using Gemini 3 Flash.
Proofreading and formatting changes by me.

editor = Skylark
date = "2025-12-27"
"""

import sys
import struct
import argparse
import os

ENCODINGS = {0: "PCM8", 1: "PCM16", 2: "DSP ADPCM", 3: "IMA ADPCM"}

def format_time(samples, rate):
    """Converts sample count to MM:SS.mmm format."""
    total_seconds = samples / rate
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    # Returns MM:SS.mmm (minutes, seconds, and milliseconds)
    return f"{minutes:01d}:{seconds:06.3f}"

def validate_bcstm(bcstm_file):
    """Checks the file header for the 'CSTM' magic bytes."""

    bcstm_file.seek(0)
    magic = bcstm_file.read(4)

    if magic != b"CSTM":
        raise ValueError(f"Invalid file format. Expected 'CSTM', found {magic.decode('ascii', 'ignore') or 'binary data'}")

def get_stream_info_pos(bcstm_file):
    """Navigates the BCSTM header to find the Stream Info start position."""

    bcstm_file.seek(0x18)
    info_block_offset = struct.unpack("<I", bcstm_file.read(4))[0]

    bcstm_file.seek(info_block_offset + 0x0C)
    stream_info_rel_offset = struct.unpack("<I", bcstm_file.read(4))[0]

    return (info_block_offset + 0x08) + stream_info_rel_offset

def get_total_samples(bcstm_file, pos):
    """Calculates the total sample count from block metadata."""

    bcstm_file.seek(pos + 0x10)
    block_count = struct.unpack("<I", bcstm_file.read(4))[0]

    bcstm_file.seek(pos + 0x18)
    samples_per_block = struct.unpack("<I", bcstm_file.read(4))[0]

    bcstm_file.seek(pos + 0x20)
    last_block_samples = struct.unpack("<I", bcstm_file.read(4))[0]

    return (block_count - 1) * samples_per_block + last_block_samples

def patch_bcstm(args):
    if not os.path.exists(args.file):
        print(f"[!] File not found: {args.file}")
        return

    try:
        mode = "rb" if args.info else "r+b"

        with open(args.file, mode) as bcstm_file:
            # Step 1: Validate Header (Skip if -f is provided)
            if not args.force:
                validate_bcstm(bcstm_file)
            else:
                print("[!] Bypassing header validation...")
            
            pos = get_stream_info_pos(bcstm_file)
            total_samples = get_total_samples(bcstm_file, pos)
            
            # --- READ EXISTING DATA ---
            bcstm_file.seek(pos)
            data = bcstm_file.read(0x14)
            encoding, loop_flag, channels = struct.unpack("BBB", data[0:3])
            sample_rate = struct.unpack("<I", data[4:8])[0]
            loop_start = struct.unpack("<I", data[8:12])[0]
            loop_end = struct.unpack("<I", data[12:16])[0]

            if args.info:
                print(f"\n--- BCSTM Stream Info: {os.path.basename(args.file)} ---")
                print(f"Encoding:      {ENCODINGS.get(encoding, 'Unknown')} ({encoding})")
                print(f"Sample Rate:   {sample_rate} Hz")
                print(f"Total Length:  {total_samples} samples ({format_time(total_samples, sample_rate)})")
                print(f"Looping:       {'Enabled' if loop_flag == 1 else 'Disabled'}")
                print(f"Loop Start:    {loop_start} samples ({format_time(loop_start, sample_rate)})")
                print(f"Loop End:      {loop_end} samples ({format_time(loop_end, sample_rate)})")
                return

            # --- SAFETY CHECKS ---
            if args.end and args.end > total_samples:
                print(f"[!] Warning: Provided Loop End ({args.end}) exceeds total file samples ({total_samples})!")
                
                confirm = input("    Proceed anyway? (y/n): ")
                if confirm.lower() != 'y': return

            # --- WRITE CHANGES ---
            # Set Loop Flag: 0 (disabled) if -n is used, else 1 (enabled)
            new_loop_val = 0 if args.no_loop else 1

            bcstm_file.seek(pos + 0x01)
            bcstm_file.write(struct.pack("B", new_loop_val))
            
            if args.start is not None:
                bcstm_file.seek(pos + 0x08)
                bcstm_file.write(struct.pack("<I", args.start))
            
            if args.end is not None:
                bcstm_file.seek(pos + 0x0C)
                bcstm_file.write(struct.pack("<I", args.end))

            print(f"\n[+] Patch complete. Loop set to: {bool(new_loop_val)}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BCSTM Looping Utility")
    parser.add_argument("file", help="Path to the .bcstm file")
    parser.add_argument("-i", "--info", action="store_true", help="Display stream info and exit")
    parser.add_argument("-f", "--force", action="store_true", help="Skip header validation check")
    parser.add_argument("-n", "--no-loop", action="store_true", help="Set the loop flag to False (0)")
    parser.add_argument("-s", "--start", type=int, help="Set loop start sample")
    parser.add_argument("-e", "--end", type=int, help="Set loop end sample")

    args = parser.parse_args()
    patch_bcstm(args)
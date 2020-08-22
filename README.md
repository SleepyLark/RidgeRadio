# RidgeRadio
Replace music for "Ridge Racer 3D" on the 3DS with other audio

## Overview
I've been playing this game a lot recently, but personally didn't like the soundtrack as much, so I replaced it with one that many people adore: "**R4: Ridge Racer Type 4**".  Some songs weren't long enough or didn't match the "racing vibe" so I used some songs from the 20th Anniversary soundtrack instead.  There also wasn't enough songs so I put in some from racing genres I liked.  Hopefully I can add more versions in the future, if not here's the song listing for the game if you wanted to make your own: [Google Sheets](https://docs.google.com/spreadsheets/d/1tvWAFrt8B4A_8jrB4CWcYzXcr7xbu70iIZDO5uSWQ-g/edit?usp=sharing)

## Mods
## R4 OST
The opening movie has been replaced with [this video](https://www.youtube.com/watch?v=MOrliq8cvSo)

**Track listing**:

Starting Grid song: Spiral Ahead

**Disc 1**
1. URBAN FRAGMENTS
2. Your Vibe (J99 Remix)
3. On Your Way
4. Naked Glow (20th Anniv. mix)
5. Spiral Ahead (Ryo Watanabe Remix)

**Disc 2**
1. Pearl Blue Soul
2. Naked Glow
3. Your Vibe
4. Lucid Rhythms
5. Thru

**Disc 3**
1. Silhouette Dance
2. Burning Rubber
3. Revlimit Funk
4. Quiet Curves
5. Motor Species

**Disc 4**
1. The Objective
2. Move Me
3. The Ride
4. Movin' In Circles
5. Thru (Sampling Masters MEGA Remix)

**Disc 5**
1. Silhouette Dance (Sampling Masters AYA Remix)
2. RIDGE RACER -one more win-
3. Burning Rubber (Takeshi Nakatsuka's Re-edit)
4. Motor Species (20th Anniv. Mix)
5. Movin' In Circles (20th Anniv. Mix)

**Disc 6**
1. Running In The 90s (Initial D)
2. GAS GAS GAS (Initial D)
3. Deja Vu (Initial D)
4. Super Sonic Racing (Vocal Version) (Sonic R)
5. Living In The City (Vocal Version) (Sonic R)

**Disc SP**

*No changes* (I haven't unlocked it yet so it's not worth replacing at the moment)

## No Backseat Driving
I found the commentary while racing to be childish and rather annoying, so instead of turning the voices off in the settings I just replaced all the driving voice clips to be empty.  You can edit it by deleting which ones you want to play since I didn't have time to listen and mark what each were saying.

## How To Install
**You will need an application that can extract `.7z` files**
### Luma
The recommended method is to use [ModMoon](https://github.com/Swiftloke/ModMoon) as it allows you to change between patched and unpatched and is already formatted for it.
#### ModMoon
- Hold Select while booting your 3DS and enable game patching in the Luma configuration menu.
- On your SD card, put the `000400000003XX00` folder into `3ds/ModMoon/`
- Rename the **XX** in the folder name to match the TitleID of your game:
- USA = 0004000000035800
- EUR = 0004000000033B00
- JPN = 0004000000032800
- Inside that folder, change the *X* in `Slot_X` to any number (i.e. "Slot_1", "Slot_2")
- Insert your SD card, restart the system, and select the mod in ModMoon.

If you're having troubles with ModMoon look [here](https://gbatemp.net/threads/modmoon-a-beautiful-simple-and-compact-mods-manager-for-the-nintendo-3ds.519080/) or just follow the instructions below.

#### Luma's LayeredFS
- Hold Select while booting your 3DS and enable game patching in the Luma configuration menu.
- On your SD card, put the RomFS folder from `000400000003XX00/Slot_X/` into `luma/titles/000400000003XX00`
- Rename the **XX** in the folder name to match the TitleID of your game:
- USA = 000400000003**58**00
- EUR = 000400000003**3B**00
- JPN = 000400000003**28**00
- Insert your SD card, restart the system, and changes should take place when you launch the game.

### Citra
- put the RomFS folder from `000400000003XX00/Slot_X/` in "%AppData%\Citra\load\mods\000400000003**XX**00" (by default) to apply the mod on Citra Canary

Alternatively you can repack the RomFS folder into the game to save some space, however I don't know of a good guide for that.


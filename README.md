[<img src="images/minecraft.svg" width="64" alt="Fabric icon">](https://www.minecraft.net/en-us/store/minecraft-deluxe-collection-pc) [<img src="images/fabric.png" width="64" alt="Fabric icon">](https://fabricmc.net/) [<img src="images/forge.jpeg" width="64" alt="Forge icon">](https://files.minecraftforge.net/net/minecraftforge/forge/) [<img src="images/neoforge.png" width="64" alt="NeoForge icon">](https://neoforged.net/) [<img src="images/curseforge.png" width="64" alt="CurseForge icon">](https://www.curseforge.com/) [<img src="images/modrinth.webp" width="64" alt="Modrinth icon">](https://modrinth.com/)  

# HelloMCWorld

![HelloMCWorld on NeoForge](images/hellomcworld_neoforge.png "HelloMCWorld on NeoForge")

"Hello MC World!!" mod

[日本語はこちら](README_ja.md)

This is an example mod that displays "Hello, world" in the chat GUI when user login to world.

It is displayed using common code (Kotlin) in the Fabric/Forge/NeoForge mod loader.

See common/src/kotlin/.../hellomcworld/HelloMCWorld.kt

## Mods required other than the mod loader

- Fabric
  - [Fabric API](https://modrinth.com/mod/fabric-api)
  - [Fabric Language Kotlin](https://modrinth.com/mod/fabric-language-kotlin)

## Development environment

- [SDKMAN!](https://sdkman.io/install)
  - [OpenJDK 21.x.x](https://sdkman.io/jdks/open)
- (Windows)[Windows PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows)
- (append: IDE) [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download/) or [VSCode](https://code.visualstudio.com/)

## Build

### Windows

#### Windows PowerShell

- Build

``` powershell
MC_VER=1.21.8 python python\\build.py
```

- Clean

``` powershell
python python\\build_clean.py
```

### Linux/macOS

#### shell

- Build

``` bash
MC_VER=1.21.8 python python/build.py
```

- Clean

``` bash
python python/build_clean.py
```

### IntelliJ IDEA Community Edition

![Build on IntelliJ IDEA](images/hellomcworld_build_intellij.png "Build on IntelliJ IDEA")

- Build

Gradle -> Tasks -> build -> build

- Clean

Gradle -> Tasks -> build -> clean

### VSCode

![Build on VSCode](images/hellomcworld_build_vscode.png "[Build on VSCode")

- Build

task -> Build with MC_VER

- Clean

task -> Clean

## Artifacts

`hellomcworld-x.x.x.jar`  
will be generated in each of the `fabric/forge/neoforge`'s `build/libs` directories, so place it in the Minecraft's `mods` directory.

# Donation!

[![Buy Me a Coffee](https://img.shields.io/badge/buy_me_an-emerald_coffee!-3C9A3C?style=for-the-badge&logo=minecraft)](https://coff.ee/azo234) ☕💚

[![Sponsor with Diamond](https://img.shields.io/badge/please-diamond_sponsor_me!-00ccff?style=for-the-badge&logo=minecraft)](https://github.com/sponsors/azo234) 💎✨

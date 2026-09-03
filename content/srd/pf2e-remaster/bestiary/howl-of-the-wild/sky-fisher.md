---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sky Fisher"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/huge
statblock: inline
name: "Sky Fisher"
level: 11
source: "Howl of the Wild"
aon_id: "creature-3310"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3310"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Sky Fisher"
level: "Creature 11"
size: "Huge"
trait_01: "Animal"
modifier: 18
perception:
  - name: "Perception"
    desc: "Perception +18; darkvision"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +21, Stealth +23"
abilityMods: [5, 7, 7, -4, 0, -3]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +22; __Ref__: +22; __Will__: +15"
hp: 200
health:
  - name: "HP"
    desc: "200; __Immunities__ precision; __Resistances__ bludgeoning 14, poison 14; __Weaknesses__ piercing 7, slashing 7"
abilities_mid:
  - name: "Transparency"
    desc: "Unless it has fed recently, the sky fisher is naturally invisible. Using non-hostile actions does not cause the sky fisher to become hidden. When it takes a hostile action of any kind, the sky fisher is hidden instead of undetected until the start of its next turn, as the vague outline of its many tendrils temporarily becomes faintly visible."
speed: "fly 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ stinging tentacle +24 (Agile, reach 30 feet) __Damage__ 2d8+8 bludgeoning plus sky fisher venom and Grab"
abilities_bot:
  - name: "Abduct"
    desc: "⬻ (Attack) The sky fisher reels in a target grabbed by its tentacles, pulling them into an adjacent space, and then attempts to Swallow them Whole (Large, 3d8+12 acid, Rupture 25). The sky fisher can only use Swallow Whole when using Abduct."
  - name: "Enzymic Vent"
    desc: "⬺ (Poison) The sky fisher vents flesh-eating enzymes into the air, dealing 3d6 persistent acid damage and 3d6 persistent bleed damage in a 20-foot emanation (DC 25 basic Reflex save). It can't use Enzymic Vent again for 1d4 rounds."
  - name: "Jet"
    desc: "⬺ (Move) The sky fisher quickly expels some of its gases to move swiftly through the air, Flying up to 100 feet in a straight line; this movement doesn't trigger reactions."
  - name: "Sky Fisher Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "3d6 poison damage, clumsy 1, and can't speak above a whisper (1 round)"
  - name: "Stage 2"
    desc: "3d8 poison damage, clumsy 2, and can't speak (1 round)"
  - name: "Stage 3"
    desc: "3d10 poison damage and paralyzed (1 round)"
sourcebook: "_Howl of the Wild_, page 181."
```

```encounter-table
name: Sky Fisher
creatures:
  - 1: Sky Fisher
```

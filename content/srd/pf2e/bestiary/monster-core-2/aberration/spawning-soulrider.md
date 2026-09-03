---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spawning Soulrider"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/soulrider
  - pf2e/creature/trait/small
statblock: inline
name: "Spawning Soulrider"
level: 1
source: "Monster Core 2"
aon_id: "creature-4558"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4558"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Spawning Soulrider"
level: "Creature 1"
size: "Small"
trait_01: "Aberration"
trait_02: "Soulrider"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [1, 3, 4, -2, 3, -1]
abilities_top:
  - name: "Celestial Flare"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) Each enemy within 30 feet of the soulrider takes 2d6 spirit damage (DC 17 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save). Creatures that fail the save are blinded for 1 round. The spawning soulrider can't use Celestial Flare again for 1 minute."
  - name: "Fiendish Lunge"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) The spawning soulrider [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Swim|Swims]] twice, making a tail Strike at any point during its movement. The Strike deals an additional 1d4 spirit damage."
  - name: "Monitor Escape"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleport]]) The soulrider's form blurs as it exploits loopholes in the multiverse. It teleports to an empty space within 60 feet."
  - name: "Recall Knowledge - Aberration"
    desc: "([[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]]): DC 15"
  - name: "Unspecific Lore"
    desc: ": DC 13"
  - name: "Specific Lore"
    desc: ": DC 10 [[srd/pf2e/bestiary/monster-core-2/aberration/spawning-soulrider|Spawning Soulrider]] Small Aberration Soulrider"
  - name: "Planar Adaptation"
    desc: "A spawning soulrider has traits appropriate to the planar energy it's absorbed: [[srd/pf2e/compendium/rules-elements/traits/player-core/celestial|celestial]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fiend|fiend]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/monitor|monitor]]."
  - name: "Swim the Dead Roads"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]]) In a process that takes 1 week, a spawning soulrider can travel through channels in the multiverse only it can sense, moving from the Outer Sphere plane whose energy it has absorbed to the Dead Roads that connect the [[srd/pf2e/compendium/gm/planes#Boneyard|Boneyard]] to the mortal Universe. From there, it travels to a random place in [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] that can support life."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +10; __Ref__: +7; __Will__: +4"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "20 feet, swim 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sucker +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ soul attach"
  - name: "Melee"
    desc: "⬻ tail +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sanctified|sanctified]]) __Damage__ 1d4+1 bludgeoning plus 1 spirit"
abilities_bot:
  - name: "Grind Soul"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/sanctified|Sanctified]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]])"
  - name: "Requirements"
    desc: "The spawning soulrider is attached to a creature's soul"
  - name: "Effect"
    desc: "The soulrider grinds the creature's soul with its jagged inner mouth, dealing 2d8 spirit damage (DC 16 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Will save). On a critical failure, the creature also takes 1d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent spirit damage]]. Regardless of the result, the spawning soulrider is no longer attached to the creature."
  - name: "Propulsive Launch"
    desc: "⬺ The spawning soulrider [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]] up to 40 feet, then makes a sucker Strike. If it's in the air and not attached to a creature after the [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]], it [[srd/pf2e/books/player-core/chapter-8-playing-the-game/movement#Falling|falls]]."
  - name: "Soul Attach"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|Spirit]]) When a spawning soulrider succeeds at a sucker Strike against a target with a soul capable of facing judgment, its sucker attaches it to that soul. While attached, both the spawning soulrider and the host creature are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]], and the spawning soulrider moves with its host until the spawning soulrider dies or the host pulls it loose ([[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] DC 16). If the host dies while the spawning soulrider is attached, the spawning soulrider disappears immediately to follow the soul leaving the body. A creature returned to life before reaching its final destination generally returns with any attached spawning soulrider."
  - name: "Tail Thrash"
    desc: "⬺"
  - name: "Requirements"
    desc: "The spawning soulrider is attached to a creature's soul"
  - name: "Effect"
    desc: "The spawning soulrider makes a tail Strike against the creature whose soul it's attached to, then one against another creature adjacent to the original target. These Strikes count towards the spawning soulrider's multiple attack penalty, but it doesn't increase until after the second attack."
sourcebook: "_Monster Core 2_, page 297."
```

```encounter-table
name: Spawning Soulrider
creatures:
  - 1: Spawning Soulrider
```

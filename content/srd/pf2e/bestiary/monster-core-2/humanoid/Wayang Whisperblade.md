---
noteType: pf2eMonster
aliases: "Wayang Whisperblade"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/wayang
  - pf2e/creature/trait/small
statblock: inline
name: "Wayang Whisperblade"
level: 1
source: "Monster Core 2"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4615"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wayang Whisperblade"
level: "Creature 1"
size: "Small"
trait_01: "Humanoid"
trait_02: "Shadow"
trait_03: "Uncommon"
trait_04: "Wayang"
modifier: 9
perception:
  - name: "Perception"
    desc: "+9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]], Wayang"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/Lore|Netherworld Lore]] +6, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +6, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +6, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +7"
abilityMods: [0, 4, 1, 3, 0, 1]
abilities_top:
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/weapons/knife/Kukri|Kukri]] (2), [[srd/pf2e/compendium/equipment/Armor#Leather Armor|Leather Armor]]"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +6; __Ref__: +9; __Will__: +5 +1 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Darkness|darkness]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Shadow|shadow]]"
hp: 19
health:
  - name: "HP"
    desc: "19"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ kukri +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|trip]]) __Damage__ 1d6 slashing"
abilities_bot:
  - name: "Shadowplay"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Illusion|Illusion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Shadow|shadow]])"
  - name: "Requirements"
    desc: "The wayang's last action was a melee [[srd/pf2e/compendium/rules-elements/actions/player-core#Strike|Strike]] that damaged their opponent"
  - name: "Effect"
    desc: "The wayang attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Tumble Through|Tumble Through]] the opponent's space, with a +2 circumstance bonus to the [[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] check. If they succeed, the wayang leaves a shadowy afterimage in their original space, which provides [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Movement#Flanking|flanking]] against the opponent until the beginning of the wayang's next turn (usually making them [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the wayang's melee attacks)."
  - name: "Sneak Attack"
    desc: "The wayang deals an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core 2_, page 353."
```

```encounter-table
name: Wayang Whisperblade
creatures:
  - 1: Wayang Whisperblade
```

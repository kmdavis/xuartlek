---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jinkin"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/gremlin
  - pf2e/creature/trait/tiny
statblock: inline
name: "Jinkin"
level: 1
source: "Monster Core"
aon_id: "creature-3033"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3033"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jinkin"
level: "Creature 1"
size: "Tiny"
trait_01: "Fey"
trait_02: "Gremlin"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +7, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +5, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +7, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +7"
abilityMods: [-2, 4, 0, 2, 2, 2]
abilities_top:
  - name: "Items"
    desc: "Shortsword"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +6; __Ref__: +10; __Will__: +7"
hp: 19
health:
  - name: "HP"
    desc: "19; __Weaknesses__ cold iron 2"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +9 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6–2 piercing"
abilities_bot:
  - name: "Sneak Attack"
    desc: "The jinkin deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
  - name: "Tinker"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) A group of six jinkins can work together for an hour to imbue an item with a curse at a range of 60 feet. While this process is lengthy, it's also unobtrusive and can be performed while [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hiding]]. Jinkins prefer to use this ability on magic items. The curse makes the item unreliable (DC 5 flat check or waste any action to Interact with or Activate the item), adds a bizarre requirement to use the item, or imparts some other curse of a similar caliber."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/prestidigitation|Prestidigitation]]"
sourcebook: "_Monster Core_, page 181."
```

```encounter-table
name: Jinkin
creatures:
  - 1: Jinkin
```

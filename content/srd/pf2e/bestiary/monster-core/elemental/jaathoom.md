---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jaathoom"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/large
statblock: inline
name: "Jaathoom"
level: 5
source: "Monster Core"
aon_id: "creature-3003"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3003"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jaathoom"
level: "Creature 5"
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Genie"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]]; (can't speak any language); cloud of visions"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +14, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +11, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +9, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +13, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +9, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [4, 5, 2, 2, 2, 4]
abilities_top:
  - name: "Cloud of Visions"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 60 feet. A jaathoom has telepathy 60 feet but can only show images, not speak."
  - name: "Items"
    desc: "Scimitar"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +14; __Will__: +11"
hp: 55
health:
  - name: "HP"
    desc: "55"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The jaathoom is [[srd/pf2e/compendium/rules-elements/conditions#Invisible|invisible]] at all times, though when they take a hostile action of any kind, they are [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] instead of [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] until the start of their next turn, as the vague outline of their form is faintly visible for a short period of time."
  - name: "Turbulent Skies"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]]) 20 feet. All squares in the emanation are difficult terrain for Striding and Flying creatures. Creatures with the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait are immune. The jaathoom can activate or deactivate this aura as a single action with the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crashing wind +16 ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], range increment 20 feet) __Damage__ 1d8+8 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) The jaathoom transforms into a Small or Medium [[srd/pf2e/compendium/gm/creature-families/elemental-air|air elemental]] or aerial [[srd/pf2e/compendium/rules-elements/traits/player-core/animal|animal]], such as an owl. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Hurricane Blast"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/air|Air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The jaathoom moves all creatures without the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]] trait in their turbulent skies aura 20 feet directly away, clockwise, or counterclockwise. A creature avoids being moved if it succeeds at a DC 21 Fortitude save."
  - name: "Ominous Dreams"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|Prediction]]) The jaathoom sends a prophetic dream to a sleeping creature within 10 feet. An unwilling creature avoids the vision if it succeeds at a DC 23 Will save. The jaathoom chooses the dream's subject, but not its exact events. The target sees a brief vision of its future related to that subject, with the effect of [[srd/pf2e/compendium/spells/rank-2/augury|_augury_]]. If the result is bad or mixed, the creature is [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]] and can't recover from being frightened until it wakes. Jaathoom Shuyookhs Jaathoom shuyookhs prefer to manifest wishes informed by their visions of the future. They add the following innate spells: __5th__ [[srd/pf2e/compendium/spells/rank-2/illusory-creature|_illusory creature_]], [[srd/pf2e/compendium/spells/rank-1/illusory-object|_illusory object_]], [[srd/pf2e/compendium/spells/rank-4/nightmare|_nightmare_]] (×2), [[srd/pf2e/compendium/spells/rank-1/sleep|_sleep_]] (×2); __4th__ [[srd/pf2e/compendium/spells/rank-1/ill-omen|_ill omen_]]."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 21 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/ill-omen|Ill Omen]], [[srd/pf2e/compendium/spells/rank-2/illusory-creature|Illusory Creature]], [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]], [[srd/pf2e/compendium/spells/rank-1/sleep|Sleep]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/nightmare|Nightmare]], [[srd/pf2e/compendium/spells/rank-4/vapor-form|Vapor Form]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (to [[srd/pf2e/compendium/equipment/runes/astral-greater|Astral Plane]]; Elemental Planes; or [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] only)"
sourcebook: "_Monster Core_, page 157."
```

```encounter-table
name: Jaathoom
creatures:
  - 1: Jaathoom
```

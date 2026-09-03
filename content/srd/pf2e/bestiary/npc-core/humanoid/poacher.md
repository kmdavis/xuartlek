---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Poacher"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Poacher"
level: 2
source: "NPC Core"
aon_id: "creature-3469"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3469"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Poacher"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +4, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +4, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [2, 4, 1, 0, 3, 0]
abilities_top:
  - name: "Expert Subsistence"
    desc: "While using [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Subsist|Subsist]], if the poacher rolls any result worse than a success, they get a success. On a success, they can provide subsistence living for themselves and four additional creatures, and on a critical success, they can take care of twice as many creatures as on a success"
  - name: "Snare Crafting"
    desc: "The poacher knows how to craft the following [[srd/pf2e/books/player-core-2/snares/index|snares]]: [[srd/pf2e/compendium/equipment/snares/alarm-snare|alarm snare]], [[srd/pf2e/compendium/equipment/snares/hampering-snare|hampering snare]], [[srd/pf2e/compendium/equipment/snares/marking-snare|marking snare]], and [[srd/pf2e/compendium/equipment/snares/signaling-snare|signaling snare]]. The poacher can create up to four snares each day without paying for the materials, using 3 Interact actions to deploy a snare. The snare becomes inert after 24 hours."
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), Light Mace, Padded Armor, snare toolkit (functions as [[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|artisan's toolkit]])"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +10; __Will__: +7"
hp: 30
health:
  - name: "HP"
    desc: "30"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light mace +11 __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ composite shortbow +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 1d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/propulsive|Propulsive]], range increment 60 feet, reload 0) __Damage__ 1d6+3 piercing"
abilities_bot:
  - name: "On the Hunt"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) The poacher designates one creature they're observing or tracking as their prey. The poacher gains a +2 circumstance bonus to Perception checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Seek|Seek]] the prey and to [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] checks to [[srd/pf2e/compendium/rules-elements/actions/player-core#Track|Track]] the prey. The first time the poacher hits the designated prey in a round, they deal an additional 1d4 precision damage. These effects last until the poacher uses On the Hunt again. Penalties For Poaching Punishment for poaching on noble land can be vicious. Maiming poachers by removing fingers is a common practice. Crueler punishments include snaring poachers in their own traps and leaving them helpless, binding them in the bloody skins of their catch, and setting dogs to chase them through the woods."
sourcebook: "_NPC Core_, page 53."
```

```encounter-table
name: Poacher
creatures:
  - 1: Poacher
```

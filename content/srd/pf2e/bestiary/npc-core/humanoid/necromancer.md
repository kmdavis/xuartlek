---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Necromancer"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Necromancer"
level: 5
source: "NPC Core"
aon_id: "creature-3538"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3538"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Necromancer"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +11, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +8, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +13"
abilityMods: [2, 3, 2, 4, 2, -1]
abilities_top:
  - name: "Stench of Decay"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) The necromancer emits a scent of putrid rot in a 5-foot emanation. A living creature that enters or begins its turn in the aura is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]."
  - name: "Items"
    desc: "hooded robe, Light Mace"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +11; __Ref__: +12; __Will__: +11"
hp: 65
health:
  - name: "HP"
    desc: "65"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ light mace +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shove|Shove]]) __Damage__ 1d4+8 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+8 bludgeoning"
abilities_bot:
  - name: "Requirements"
    desc: "The necromancer has at least one undead entity active"
  - name: "Effect"
    desc: "The necromancer commands all their undead entities to attack. Each entity can Stride up to 20 feet into an empty square and make a Strike. The Strike has a +15 attack modifier and deals 2d12 bludgeoning damage (or spirit damage if the entity is a spirit). The Strike has the [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]] trait, and no multiple attack penalty applies to it."
  - name: "Wave of Death"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|Void]])"
  - name: "Requirements"
    desc: "The necromancer isn't [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] and has at least one undead entity active"
  - name: "Effect"
    desc: "The necromancer overloads their undead entities with void energy, causing all of them to explode. Each entity is destroyed, dealing 4d12 void damage to each creature in a 10-foot emanation with a DC 23 basic Fortitude save. A creature in more than one explosion is damaged only once. The necromancer becomes drained 1."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] __Undead, Arise!__ ⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The necromancer summons two Medium undead entities in different empty squares up to 30 feet away. These undead entities can take the form of zombies, skeletons, or ghosts, chosen by the necromancer. The entities block movement as though they were creatures and can be attacked. Each entity has 1 Hit Point and the same AC and saves as the necromancer. They can't take actions of their own and deteriorate if the necromancer is reduced to 0 Hit Points. The necromancer can have up to four undead entities at any given time. If they call another, the oldest undead entity deteriorates. __Undead, Attack!__ ⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
sourcebook: "_NPC Core_, page 99."
```

```encounter-table
name: Necromancer
creatures:
  - 1: Necromancer
```

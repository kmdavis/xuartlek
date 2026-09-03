---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nightwood Guardian"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/troll
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Nightwood Guardian"
level: 9
source: "Rage of Elements"
aon_id: "creature-2685"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2685"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Nightwood Guardian"
level: "Creature 9"
size: "Large"
trait_01: "Giant"
trait_02: "Troll"
trait_03: "Uncommon"
trait_04: "Wood"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/languages#Jotun|Jotun]], [[srd/pf2e/compendium/rules-elements/languages#Muan|Muan]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +21, Nightwood Lore +15"
abilityMods: [6, 3, 6, 0, 2, 2]
abilities_top:
  - name: "Light Blindness"
    desc: ""
  - name: "Items"
    desc: "Club, elemental wooden shield (Hardness 8, Hit Points 64, BT 32)"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +21; __Ref__: +16; __Will__: +17"
hp: 200
health:
  - name: "HP"
    desc: "200 (flesh of wood); __Weaknesses__ axes 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10"
abilities_mid:
  - name: "Fire-fueled Rage"
    desc: "When a nightwood guardian takes fire damage, they become enraged. The guardian gains 15 temporary Hit Points, deals 2 additional damage with melee Strikes, and has a –1 penalty to AC. They can't Raise their Shield or use actions with the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait except for Seek. This effect ends when the nightwood guardian no longer observes any fire for 1 round or when they fall [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], whichever comes first."
  - name: "Flesh of Wood"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/wood|wood]]) Wounds inflicted on a nightwood guardian turn their flesh to wood. When the guardian is reduced to 40 HP or fewer, their body becomes solid wood. They are [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]], have resistance 10 to all damage, and have regeneration 40 (deactivated by fire). This ends once the guardian has 100 HP or more, though they can choose to stay in this form indefinitely."
  - name: "Shield Eyes"
    desc: "When a nightwood guardian has their shield raised, they protect their eyes, losing the [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] and [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] conditions from light blindness and other [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]] effects."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shield Block"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ club +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d12+6 piercing"
abilities_bot:
  - name: "Nightwood Roar"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/darkness|Darkness]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The guardian roars, snuffing out lights in a 30-foot cone. Ordinary flames and lights are extinguished, and the guardian attempts to counteract any magical light with a +21 counteract modifier and a counteract rank of 5. Rare Gentleness Though most encounters with nightwood guardians end in violence, the [[srd/pf2e/compendium/gm/planes#Plane of Wood|Plane of Wood]] has many folktales about these giant creatures escorting youngsters lost in the nightwoods safely out of the darkness. Whether these stories are true or wishful thinking is debated, with some arguing that a nightwood guardian would only perform such a kindness on the orders of another creature"
sourcebook: "_Rage of Elements_, page 216."
```

```encounter-table
name: Nightwood Guardian
creatures:
  - 1: Nightwood Guardian
```

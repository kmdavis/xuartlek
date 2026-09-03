---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Interlocutor"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/large
statblock: inline
name: "Interlocutor"
level: 12
source: "Monster Core 2"
aon_id: "creature-4610"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4610"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Interlocutor"
level: "Creature 12"
size: "Large"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; greater darkvision, painsight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +22, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +25, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +26, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +22, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +19, [[srd/pf2e/compendium/rules-elements/skills/lore|Torture Lore]] +20"
abilityMods: [7, 3, 5, 2, 6, 5]
abilities_top:
  - name: "Painsight"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A velstrac automatically knows whether a creature it sees has any of the [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]], and [[srd/pf2e/compendium/rules-elements/conditions#Wounded|wounded]] conditions as well as the value of those conditions."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +21; __Will__: +26 +1 status to all saves vs. magic"
hp: 215
health:
  - name: "HP"
    desc: "215 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] or [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ holy 15, silver 15"
abilities_mid:
  - name: "Glimpse of Stolen Flesh"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 30 feet. When a creature ends its turn in the aura, it sees pieces of its own body amid the interlocutor's form. The creature must succeed at a DC 29 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]] 1."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Shadow Siphon"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/shadow|shadow]])"
  - name: "Trigger"
    desc: "The interlocutor would take damage from a spell or magical effect"
  - name: "Effect"
    desc: "The interlocutor takes half the triggering damage instead."
speed: "40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly 2d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d10+13 slashing plus 2d6 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) The interlocutor stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against glimpse of stolen flesh. In addition, if the creature was already [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]], on a failed save, it feels its internal organs twist and writhe, and is [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy]] 2 for 1 minute. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the interlocutor's next turn."
  - name: "Surgical Rend"
    desc: "⬻ This functions as the Rend ability, dealing claw Strike damage. In addition, if the target is a living creature with organs and muscle, the interlocutor opens a precise wound. Until the creature is restored to its maximum Hit Points, thus closing the wound, Strikes against the creature deal an additional 1d6 precision damage."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×2), [[srd/pf2e/compendium/spells/rank-2/sound-body|Sound Body]] (×2) - __5th__ [[srd/pf2e/compendium/spells/rank-5/breath-of-life|Breath of Life]] - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (self only; to [[srd/pf2e/compendium/gm/planes#The Netherworld|the Netherworld]] or [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] only)"
sourcebook: "_Monster Core 2_, page 347."
```

```encounter-table
name: Interlocutor
creatures:
  - 1: Interlocutor
```

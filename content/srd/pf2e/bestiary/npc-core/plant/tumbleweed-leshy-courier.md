---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Tumbleweed Leshy Courier"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Tumbleweed Leshy Courier"
level: 3
source: "NPC Core"
aon_id: "creature-3657"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3657"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Tumbleweed Leshy Courier"
level: "Creature 3"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]; [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|_speak with plants_]] (tumbleweeds and scrubland brush only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +8, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +7, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +9, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [1, 4, 1, 0, 2, 2]
abilities_top:
  - name: "Tumbling Traveler"
    desc: "The tumbleweed leshy courier gains a +10-foot circumstance bonus to Speed while traveling during exploration mode."
  - name: "Items"
    desc: "Crossbow (20 bolts), Dagger"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +6; __Ref__: +12; __Will__: +9"
hp: 35
health:
  - name: "HP"
    desc: "35"
abilities_mid:
  - name: "Spiny Burst"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) When the tumbleweed leshy courier dies, a burst of primal energy explodes from their body, restoring 2d8 Hit Points to each plant creature in a 30-foot emanation. This area immediately fills with brambles and thistles, becoming difficult terrain. Any creature that moves through the area takes 1 piercing damage per square traversed. If the terrain is not a viable environment for these plants, they wither after 24 hours."
  - name: "Nimble Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "The tumbleweed leshy courier is targeted with an attack by an attacker they can see"
  - name: "Effect"
    desc: "The leshy gains a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+5 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+5 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +12 (range increment 120 feet, reload 1) __Damage__ 1d8+2 piercing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The tumbleweed leshy courier transforms into a Small tumbleweed. This ability otherwise uses the effects of [[srd/pf2e/compendium/spells/rank-2/one-with-plants|_one with plants_]]. Additionally, when the leshy uses their Change Shape ability, they still have a Speed of 10 feet for the purpose of travel during exploration mode."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17 - __Constant (3rd)__ [[srd/pf2e/compendium/spells/rank-3/speak-with-plants|Speak with Plants]] (tumbleweeds and scrubland brush only)"
sourcebook: "_NPC Core_, page 200."
```

```encounter-table
name: Tumbleweed Leshy Courier
creatures:
  - 1: Tumbleweed Leshy Courier
```

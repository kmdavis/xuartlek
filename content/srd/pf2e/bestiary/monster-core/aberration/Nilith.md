---
noteType: pf2eMonster
aliases: "Nilith"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/medium
statblock: inline
name: "Nilith"
level: 10
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3107"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nilith"
level: "Creature 10"
size: "Medium"
trait_01: "Aberration"
modifier: 19
perception:
  - name: "Perception"
    desc: "+19; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +21, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +19, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +21, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +17"
abilityMods: [3, 5, 4, 3, 3, 5]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +17; __Ref__: +20; __Will__: +20"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 10, physical 5 (except silver)"
speed: "25 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d10+9 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ fangs +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 2d12+9 piercing"
abilities_bot:
  - name: "Mind Crush"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Requirements"
    desc: "The nilith has a creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grabbed]]"
  - name: "Effect"
    desc: "The nilith reaches into the mind of the grabbed creature and implants disjointed images of the victim's worst fears and nightmares. The grabbed creature takes 6d6 mental damage with a DC 31 basic Will save. On a critical failure, the target is also affected as though by [[srd/pf2e/compendium/spells/rank-6/Never Mind|_never mind_]], and it must attempt a second Will save against that effect. From the Dreamlands The nilith's association with the remote and little-understood [[srd/pf2e/compendium/gm/Planes#Dreamlands|Dreamlands]], also known as the Dimension of Dreams, is unusual. They draw power from a latent dreaming connection to that realm, but they are native to [[srd/pf2e/compendium/gm/Planes#The Universe|the Universe]]."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-3/Dream Message|Dream Message]], [[srd/pf2e/compendium/spells/rank-4/Flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only), [[srd/pf2e/compendium/spells/rank-4/Nightmare|Nightmare]], [[srd/pf2e/compendium/spells/rank-5/Wave of Despair|Wave of Despair]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Hallucination|Hallucination]], [[srd/pf2e/compendium/spells/rank-5/Mind Probe|Mind Probe]]"
sourcebook: "_Monster Core_, page 239."
```

```encounter-table
name: Nilith
creatures:
  - 1: Nilith
```

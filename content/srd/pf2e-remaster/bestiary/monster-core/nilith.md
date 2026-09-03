---
obsidianUIMode: preview
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
aon_id: "creature-3107"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3107"
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
    desc: "Perception +19; darkvision"
languages: "Aklo, Common; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +17, Intimidation +23, Occultism +19, Stealth +21, Survival +17"
abilityMods: [3, 5, 4, 3, 3, 5]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +17; __Ref__: +20; __Will__: +20"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ mental 10, physical 5 (except silver)"
speed: "25 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +23 (Agile, Finesse, Magical) __Damage__ 2d10+9 slashing plus Grab"
  - name: "Melee"
    desc: "⬻ fangs +23 (Finesse, Magical) __Damage__ 2d12+9 piercing"
abilities_bot:
  - name: "Mind Crush"
    desc: "⬻ (Mental, Occult)"
  - name: "Requirements"
    desc: "The nilith has a creature grabbed"
  - name: "Effect"
    desc: "The nilith reaches into the mind of the grabbed creature and implants disjointed images of the victim's worst fears and nightmares. The grabbed creature takes 6d6 mental damage with a DC 31 basic Will save. On a critical failure, the target is also affected as though by _never mind_, and it must attempt a second Will save against that effect. From the Dreamlands The nilith's association with the remote and little-understood Dreamlands, also known as the Dimension of Dreams, is unusual. They draw power from a latent dreaming connection to that realm, but they are native to the Universe."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ Message, Read Aura, Shield, Telekinetic Hand - __3rd__ Mind Reading (at will) - __4th__ Confusion, Dream Message, Flicker, Invisibility (at will; self only), Nightmare, Wave of Despair - __5th__ Hallucination, Mind Probe"
sourcebook: "_Monster Core_, page 239."
```

```encounter-table
name: Nilith
creatures:
  - 1: Nilith
```

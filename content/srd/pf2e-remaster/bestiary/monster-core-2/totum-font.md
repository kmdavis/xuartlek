---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Totum Font"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/air
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/metal
  - pf2e/creature/trait/water
  - pf2e/creature/trait/wood
  - pf2e/creature/trait/large
statblock: inline
name: "Totum Font"
level: 15
source: "Monster Core 2"
aon_id: "creature-4586"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4586"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Totum Font"
level: "Creature 15"
size: "Large"
trait_01: "Air"
trait_02: "Earth"
trait_03: "Elemental"
trait_04: "Fire"
trait_05: "Metal"
trait_06: "Water"
trait_07: "Wood"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; all-around vision, darkvision"
languages: "Muan, Petran, Pyric, Sussuran, Talican, Thalassic; truespeech"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Arcana +30, Athletics +29, Crafting +30, Elemental Lore +33, Nature +31"
abilityMods: [6, 3, 4, 8, 3, 3]
abilities_top:
  - name: "Items"
    desc: "_moderate sturdy shield_ (Hardness 13^ HP 104^ BT 52)"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +26; __Ref__: +23; __Will__: +29"
hp: 325
health:
  - name: "HP"
    desc: "325"
abilities_mid:
  - name: "Elemental Attunement"
    desc: "A totum font is always attuned to a single element (air, earth, fire, metal, water, or wood), represented by which of their faces points forward. They can change this attunement to the element of their choice as a single action, or as a free action when they roll initiative."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Requirements"
    desc: "The font is attuned to air, fire, or water."
  - name: "Shield Block"
    desc: "⬲"
  - name: "Requirements"
    desc: "The font is attuned to earth, metal, or wood."
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +30 (Magical, reach 10 feet) __Damage__ 3d8+16 bludgeoning"
abilities_bot:
  - name: "Briar's Hold"
    desc: "⬺ (Concentrate, incapacitation, primal, wood)"
  - name: "Requirements"
    desc: "The font is attuned to wood"
  - name: "Effect"
    desc: "Each creature within 20 feet must succeed at a DC 36 Fortitude save or become slowed 1 for 1 minute. When a creature already slowed by Briar's Hold fails its Fortitude save, it becomes petrified for 1 minute but is turned to wood instead of stone."
  - name: "Brilliance of Flame"
    desc: "⬺ (Fire, primal)"
  - name: "Requirements"
    desc: "The font is attuned to fire"
  - name: "Effect"
    desc: "The font flies 30 feet and explodes in a fiery Elemental Eruption."
  - name: "Elemental Eruption"
    desc: "⬺ (Primal) The font explodes in a cacophony of color and energy. Each creature in a 20-foot emanation takes 9d6 damage (DC 36 basic Reflex save). The explosion deals bludgeoning damage unless the font is attuned to air (electricity damage), fire (fire damage), metal (slashing damage), or wood (piercing damage). Elemental Eruption gains the trait matching the element the font is attuned to."
  - name: "Entomb"
    desc: "⭓ (Earth)"
  - name: "Requirements"
    desc: "The font is attuned to earth, and its last action was a successful tendril Strike"
  - name: "Effect"
    desc: "The font attempts an Athletics check to Grapple the target of the Strike."
  - name: "Overflowing Tide"
    desc: "⬺ (Primal, water)"
  - name: "Requirements"
    desc: "The font is attuned to water"
  - name: "Effect"
    desc: "Elemental waves surge around the font, creating a torrential Elemental Eruption and pushing creatures in the area 20 feet (or 10 feet on a successful saving throw)."
  - name: "Serrated Flurry"
    desc: "⬻ (Metal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The font is attuned to metal"
  - name: "Effect"
    desc: "The font lashes out with two tendril Strikes, each targeting a different creature within their reach. These Strikes deal slashing damage."
  - name: "Tempest Charge"
    desc: "⬻ (Air)"
  - name: "Requirements"
    desc: "The font is attuned to air"
  - name: "Effect"
    desc: "The font Flies 60 feet and makes a tendril Strike against a creature it hasn't attacked this turn. Wellsprings Of One Without access to the balance of all six elemental planes, a totum font becomes fractured and inundated in a single element. Most were healed when the Planes of Metal and Wood returned, but some of these so-called “wellsprings of one” still wander the universe, agitated and confused."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33 - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 325."
```

```encounter-table
name: Totum Font
creatures:
  - 1: Totum Font
```

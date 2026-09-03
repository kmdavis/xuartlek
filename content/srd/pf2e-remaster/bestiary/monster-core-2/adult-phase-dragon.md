---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Phase Dragon"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Phase Dragon"
level: 13
source: "Monster Core 2"
aon_id: "creature-4355"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4355"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Phase Dragon"
level: "Creature 13"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +26, Arcana +27, Athletics +24, Diplomacy +25, Lore +29, Nature +23, Occultism +25, Religion +23"
abilityMods: [5, 7, 3, 8, 6, 5]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +20; __Ref__: +25; __Will__: +24 +2 status to all saves vs. arcane"
hp: 180
health:
  - name: "HP"
    desc: "180; __Immunities__ immobilized, paralyzed, sleep"
abilities_mid:
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to counteract any teleportation effect that targets them (counteract rank 7th, counteract modifier +25). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally. __Shoo!__ ⬲ (arcane, teleportation)"
  - name: "Trigger"
    desc: "An enemy within 15 feet damages the dragon"
  - name: "Effect"
    desc: "The dragon teleports the creature up to 25 feet away. The destination must be on the ground and in a space with no hazards."
speed: "50 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 (Magical, reach 15 feet) __Damage__ 3d12+12 piercing"
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, magical, reach 10 feet) __Damage__ 3d8+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +24 (Magical, reach 10 feet) __Damage__ 3d10+12 bludgeoning"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "⬺ (Arcane, teleportation) The dragon exhales a swirl of energy that pulls creatures apart, dealing 12d6 force damage in a 40-foot cone (DC 33 basic Reflex save). The dragon can teleport any creature that fails its save, teleporting that creature up to 40 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
  - name: "Phase Jump"
    desc: "⬻ (Arcane, concentrate, teleportation)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dragon teleports up to 75 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to Fly."
  - name: "Portal Strike"
    desc: "⬺ (Arcane, concentrate, manipulate, teleportation) The dragon momentarily opens a small portal and makes a claw Strike against a creature within 75 feet. The target is off-guard to the Strike."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 33 - __Cantrips (7th)__ Detect Magic, Read Aura - __4th__ Flicker, Planar Tether, Translocate (at will) - __5th__ Translocate - __6th__ Teleport - __Constant (7th)__ Know the Way"
sourcebook: "_Monster Core 2_, page 125."
```

```encounter-table
name: Adult Phase Dragon
creatures:
  - 1: Adult Phase Dragon
```

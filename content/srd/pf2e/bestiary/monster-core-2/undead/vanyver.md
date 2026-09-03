---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vanyver"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Vanyver"
level: 13
source: "Monster Core 2"
aon_id: "creature-4310"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4310"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Vanyver"
level: "Creature 13"
size: "Huge"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision, lifesense 60 feet"
languages: "Chthonian, Common, Diabolic, Necril; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Arcana +23, Athletics +27, Netherworld Lore +25, Religion +24, Stealth +25, Void Lore +25"
abilityMods: [8, 4, 6, 4, 5, 5]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +29; __Ref__: +23; __Will__: +22"
hp: 275
health:
  - name: "HP"
    desc: "275 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 10; __Weaknesses__ holy 10, silver 10"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "(aura, divine, void) 40 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 3d6 void damage with a DC 30 basic Fortitude save. If it fails, it's also enfeebled 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is stunned 2 and clumsy 2 as long as it remains in the sunlight."
  - name: "Catching Bite"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the vanyver's jaws makes a melee Strike against the vanyver with a weapon"
  - name: "Effect"
    desc: "The vanyver chooses to be hit. If the attack would've missed, it hits. The vanyver catches the weapon in their jaws and uses Drain Magic on it without fulfilling Drain Magic's requirements."
speed: "25 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 (Magical, reach 10 feet) __Damage__ 3d10+11 piercing plus 1d10 cold and Drain Magic"
  - name: "Melee"
    desc: "⬻ talon +27 (Magical, reach 10 feet) __Damage__ 3d10+11 bludgeoning plus 1d10 cold and Grab"
  - name: "Melee"
    desc: "⬻ wing +27 (Agile, magical, reach 15 feet) __Damage__ 3d6+11 bludgeoning plus 1d10 cold"
abilities_bot:
  - name: "Drain Magic"
    desc: "⬻"
  - name: "Requirements"
    desc: "The vanyver's last action was a successful jaws Strike against a creature, object, or spell effect"
  - name: "Effect"
    desc: "The vanyver casts an innate _dispel magic_ on the same target; if the target was a creature, the vanyver can target a spell affecting the creature instead. If a spell effect or item is successfully counteracted, the vanyver gains temporary Hit Points equal to double the counteract rank of the effect that was counteracted."
  - name: "Snatch"
    desc: "The vanyver can Fly at half Speed while they have a creature grabbed or restrained in either or both of their talons, carrying that creature along with them."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34 - __Cantrips (7th)__ Detect Magic - __4th__ Darkness, See the Unseen - __6th__ Dispel Magic (at will), Harm (×3) - __7th__ Interplanar Teleport (to the Universe; the Void; or the Netherworld only) __Constrict l 3d10+5 piercing, DC 33__ ⬻"
sourcebook: "_Monster Core 2_, page 84."
```

```encounter-table
name: Vanyver
creatures:
  - 1: Vanyver
```

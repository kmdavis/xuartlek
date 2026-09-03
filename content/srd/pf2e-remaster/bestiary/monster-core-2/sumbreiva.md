---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sumbreiva"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/void
  - pf2e/creature/trait/large
  - pf2e/creature/trait/negative
statblock: inline
name: "Sumbreiva"
level: 16
source: "Monster Core 2"
aon_id: "creature-4570"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4570"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sumbreiva"
level: "Creature 16"
size: "Large"
trait_01: "Humanoid"
trait_02: "Unholy"
trait_03: "Void"
trait_04: "Negative"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; greater darkvision, scent (imprecise) 30 feet"
languages: "Aklo, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +28, Intimidation +30, Stealth +35, Survival +29"
abilityMods: [8, 9, 3, 6, 5, 4]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +25; __Ref__: +33; __Will__: +27"
hp: 290
health:
  - name: "HP"
    desc: "290 (void healing); __Immunities__ death effects, drained"
abilities_mid:
  - name: "Hunter's Triumph"
    desc: "⬲ (auditory, emotion, fear, mental)"
  - name: "Trigger"
    desc: "The sumbreiva kills a creature"
  - name: "Effect"
    desc: "The sumbreiva lets out a triumphant, bone-chilling howl. Every enemy in a 30-foot emanation must succeed at a DC 36 Will save or become frightened 3 (and fleeing as long as it's frightened on a critical failure)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ sumbreiva huntblade +33 (Agile, death, finesse, magical, versatile S) __Damage__ 3d8+16 piercing plus huntblade brutality"
  - name: "Melee"
    desc: "⬻ shadow whip +33 (Agile, death, disarm, finesse, magical, reach 10 feet, trip) __Damage__ 3d4+16 bludgeoning plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ sumbreiva huntblade +33 (Agile, death, magical, thrown 30 feet, versatile S) __Damage__ 3d8+16 piercing plus huntblade brutality"
abilities_bot:
  - name: "Claim Trophy"
    desc: "⬻ The sumbreiva claims the soul of a creature they killed within the last minute. This works like seize soul, except that no black sapphire is required, and the soul is turned into a glowing blue light called a soul trophy. Anyone who kills the sumbreiva can then free the soul from any soul trophy by touching it and speaking the word for “freedom” in any language."
  - name: "Huntblade Brutality"
    desc: "The sumbreiva's huntblade deals an additional 2d8 precision damage to drained, frightened, or off-guard creatures."
  - name: "Whip Drain"
    desc: "⬻ (Arcane, death)"
  - name: "Requirements"
    desc: "The sumbreiva has a creature grabbed with their shadow whip"
  - name: "Effect"
    desc: "The grabbed creature must succeed at a DC 38 Fortitude save or become drained 2 (drained 3 on a critical failure). If the creature is already drained, this increases its drained value instead, to a maximum of drained 4. Superior Sumbreivas As sumbreiva hunters attain souls, they grow in power and physically transform. They might increase in stature, grow more limbs or great leathery wings, or form advanced armaments suited to their personalities and hunting methods. These outward manifestations make it easy for other sumbreivas to distinguish superior warriors from the less masterful hunters. The greatest sumbreivas are said to be inexorable giants suited for hunting only kaiju, demigods, and the spawn of Rovagug."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 36 - __4th__ Darkness, Earthbind"
sourcebook: "_Monster Core 2_, page 309."
```

```encounter-table
name: Sumbreiva
creatures:
  - 1: Sumbreiva
```

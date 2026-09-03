---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Mirage Dragon"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Mirage Dragon"
level: 9
source: "Monster Core"
aon_id: "creature-2950"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2950"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Mirage Dragon"
level: "Creature 9"
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Arcana +19, Athletics +18, Crafting +19, Deception +21, Diplomacy +19, Illusion Lore +21, Performance +19, Stealth +19, Thievery +19"
abilityMods: [5, 4, 3, 4, 5, 6]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can Hide in natural environments even if they don't have cover."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +16; __Ref__: +17; __Will__: +20 +2 status to all saves vs. arcane"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ fascinated, paralyzed, sleep"
abilities_mid:
  - name: "Scintillating Defense"
    desc: "⬲ (visual)"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "The dragon flashes their iridescent scales at the triggering creature to throw off the attack. The dragon gains concealment against the triggering attack."
speed: "40 feet, climb 20 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (Magical, reach 10 feet) __Damage__ 2d10+8 piercing"
  - name: "Melee"
    desc: "⬻ claws +20 (Agile, Magical) __Damage__ 2d6+8 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 (Magical, reach 15 feet) __Damage__ 2d8+8 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hallucinatory Breath whenever they score a critical hit with a Strike."
  - name: "Hallucinatory Breath"
    desc: "⬺ (Arcane, Emotion, Mental) The dragon breathes a cloud that assaults the senses and deals 7d6 mental damage in a 30-foot cone (DC 27 Will save). A creature that fails its save is also confused for 1 round (1 minute on a critical failure) and is then temporarily immune to being confused by Hallucinatory Breath for 1 hour. The dragon can't use Hallucinatory Breath again for 1d4 rounds."
  - name: "Lunging Bite"
    desc: "⬺ The dragon lunges their head forward, making a jaws Strike with an extended reach of 20 feet."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to off-guard targets."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 27 - __Cantrips (5th)__ Figment, Message - __2nd__ Invisibility - __4th__ Illusory Creature, Illusory Object (at will), Mirage - __5th__ Illusory Scene"
sourcebook: "_Monster Core_, page 122."
```

```encounter-table
name: Young Mirage Dragon
creatures:
  - 1: Young Mirage Dragon
```

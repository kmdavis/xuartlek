---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Conspirator Dragon"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ancient Conspirator Dragon"
level: 17
source: "Monster Core"
aon_id: "creature-2937"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2937"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Conspirator Dragon"
level: "Creature 17"
size: "Huge"
trait_01: "Dragon"
trait_02: "Occult"
trait_03: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; (32 to Sense Motive) darkvision, scent (imprecise) 60 feet"
languages: "Aklo, Common, Draconic, Shadowtongue, Sussuran; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +30, Deception +35, Diplomacy +33, Intimidation +33, Lore +31, Occultism +31, Performance +35, Society +31, Stealth +30"
abilityMods: [9, 5, 6, 6, 7, 8]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +27; __Ref__: +28; __Will__: +32 +2 status to all saves vs. occult"
hp: 345
health:
  - name: "HP"
    desc: "345; __Immunities__ controlled, paralyzed, sleep"
abilities_mid:
  - name: "Retract Body"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is hit or critically hit by an attack made by a creature the dragon can see"
  - name: "Effect"
    desc: "The dragon retracts the targeted body part or twists away to avoid the attack, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "50 feet, climb 50 feet, fly 200 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +32 (Magical, reach 15 feet) __Damage__ 3d8+17 piercing"
  - name: "Melee"
    desc: "⬻ claw +32 (Agile, Magical, reach 10 feet) __Damage__ 3d6+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +30 (Magical, reach 20 feet) __Damage__ 2d10+17 bludgeoning"
  - name: "Ranged"
    desc: "⬻ mental blast +31 (Mental, range 100 feet) __Damage__ 6d6+6 mental"
abilities_bot:
  - name: "Conjure Disguise"
    desc: "(Manipulate, Occult, Polymorph)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The dragon conjures a perfect flesh-suit replica of a humanoid they've seen of their size or smaller and compresses themself into it, along with generating appropriate clothing for the humanoid. This process takes 1 minute to complete, during which the dragon is off-guard. If the dragon stops or is interrupted in this process, the suit is destroyed. Once the process is complete, the dragon can remain in this disguise indefinitely. The transformation has the effects of Change Shape, except that the disguise is not actively magical in nature and doesn't register as magical to _detect magic_ and similar effects. The dragon loses Retract Body while transformed. If the dragon is critically hit while wearing the disguise, the suit is destroyed and immediately explodes. This has the effects of Detonate Disguise, except that creatures use the outcome one degree of success better than they rolled on their save."
  - name: "Detonate Disguise"
    desc: "⬺ (Occult)"
  - name: "Requirements"
    desc: "The dragon is wearing their conjured disguise"
  - name: "Effect"
    desc: "The dragon erupts from the disguise, destroying it. The explosive revelation deals 18d6 bludgeoning damage to creatures in a 5-foot emanation with a DC 39 basic Reflex save. A creature that fails its save is dazzled for 1 round as it becomes covered in scraps from the disguise. Any creature sharing a space with the dragon after they erupt is pushed into the nearest empty space."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "When the dragon scores a critical hit with a Strike, they recharge Smoke Breath."
  - name: "Rushed Transformation"
    desc: "⬽ (Concentrate, Occult, Manipulate, Polymorph)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "Using the aid of magic and an exhausting amount of effort, the dragon quickly reshapes their body into the form of a generic humanoid figure. This has the effects of _humanoid form_ except that it lasts only 1 minute, and the dragon doesn't gain the +4 status bonus to Deception as the transformation makes use of the dragon's body to crudely mimic a humanoid form. The dragon can Dismiss the effect. Whenever the effect ends, the dragon leaves behind scraps of magically conjured flesh, which could give away the dragon's presence."
  - name: "Smoke Breath"
    desc: "⬺ (Occult, Poison) The dragon unleashes a noxious cloud of smoke that deals 16d6 poison damage in a 60-foot cone (DC 39 basic Fortitude save). The smoke remains for 1 minute. This has the effects of _mist_, except it fills the cone's area. The dragon can't use Smoke Breath again for 1d4 rounds."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 3d6 precision damage to off-guard targets."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 41 - __4th__ Charm (at will), Rewrite Memory (at will) - __9th__ Dominate, Mind Probe, Mind Reading (at will), Rewrite Memory"
sourcebook: "_Monster Core_, page 112."
```

```encounter-table
name: Ancient Conspirator Dragon
creatures:
  - 1: Ancient Conspirator Dragon
```

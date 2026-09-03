---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Conspirator Dragon"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Adult Conspirator Dragon"
level: 12
source: "Monster Core"
aon_id: "creature-2936"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2936"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Conspirator Dragon"
level: "Creature 12"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 23
perception:
  - name: "Perception"
    desc: "Perception +23; (25 to Sense Motive) darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Shadowtongue, Sussuran; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +21, Athletics +23, Deception +25, Diplomacy +25, Intimidation +23, Lore +25, Occultism +23, Performance +25, Society +23, Stealth +21"
abilityMods: [5, 3, 4, 5, 5, 7]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +20; __Ref__: +21; __Will__: +25 +2 status to all saves vs. occult"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ controlled, paralyzed, sleep"
abilities_mid:
  - name: "Retract Body"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is hit or critically hit by an attack made by a creature the dragon can see"
  - name: "Effect"
    desc: "The dragon retracts the targeted body part or twists away to avoid the attack, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "40 feet, climb 40 feet, fly 140 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +25 (Magical, reach 10 feet) __Damage__ 3d8+11 piercing"
  - name: "Melee"
    desc: "⬻ claw +25 (Agile, Magical) __Damage__ 3d6+11 slashing"
  - name: "Melee"
    desc: "⬻ tail +23 (Magical, reach 15 feet) __Damage__ 2d10+11 bludgeoning"
  - name: "Ranged"
    desc: "⬻ mental blast +25 (Mental, range 100 feet) __Damage__ 3d6+6 mental"
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
    desc: "The dragon erupts from the disguise, destroying it. The explosive revelation deals 13d6 bludgeoning damage to creatures in a 5-foot emanation with a DC 31 basic Reflex save. A creature that fails its save is dazzled for 1 round as it becomes covered in scraps from the disguise. Any creature sharing a space with the dragon after they erupt is pushed into the nearest empty space."
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
    desc: "⬺ (Occult, Poison) The dragon unleashes a noxious cloud of smoke that deals 10d6 poison damage in a 50-foot cone (DC 33 basic Fortitude save). The smoke remains for 1 minute. This has the effects of _mist_, except it fills the cone's area. The dragon can't use Smoke Breath again for 1d4 rounds."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to off-guard targets."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 32 - __1st__ Charm (at will) - __6th__ Charm, Mind Probe, Mind Reading (at will), Rewrite Memory"
sourcebook: "_Monster Core_, page 111."
```

```encounter-table
name: Adult Conspirator Dragon
creatures:
  - 1: Adult Conspirator Dragon
```

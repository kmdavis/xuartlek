---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2937"
socialImage: og-image.png
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
    desc: "+30; (32 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/Languages#Shadowtongue|Shadowtongue]], [[srd/pf2e/compendium/rules-elements/Languages#Sussuran|Sussuran]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +35, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +33, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +33, [[srd/pf2e/compendium/rules-elements/skills/Lore|Lore]] +31, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +31, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +35, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +31, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +30"
abilityMods: [9, 5, 6, 6, 7, 8]
ac: 40
armorclass:
  - name: "AC"
    desc: "40; __Fort__: +27; __Ref__: +28; __Will__: +32 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]"
hp: 345
health:
  - name: "HP"
    desc: "345; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/Conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]"
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
    desc: "⬻ jaws +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 15 feet]]) __Damage__ 3d8+17 piercing"
  - name: "Melee"
    desc: "⬻ claw +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d6+17 slashing"
  - name: "Melee"
    desc: "⬻ tail +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 20 feet]]) __Damage__ 2d10+17 bludgeoning"
  - name: "Ranged"
    desc: "⬻ mental blast +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], range 100 feet) __Damage__ 6d6+6 mental"
abilities_bot:
  - name: "Conjure Disguise"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The dragon conjures a perfect flesh-suit replica of a [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]] they've seen of their size or smaller and compresses themself into it, along with generating appropriate clothing for the humanoid. This process takes 1 minute to complete, during which the dragon is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]]. If the dragon stops or is interrupted in this process, the suit is destroyed. Once the process is complete, the dragon can remain in this disguise indefinitely. The transformation has the effects of Change Shape, except that the disguise is not actively magical in nature and doesn't register as [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]] to [[srd/pf2e/compendium/spells/cantrips/Detect Magic|_detect magic_]] and similar effects. The dragon loses Retract Body while transformed. If the dragon is critically hit while wearing the disguise, the suit is destroyed and immediately explodes. This has the effects of Detonate Disguise, except that creatures use the outcome one degree of success better than they rolled on their save."
  - name: "Detonate Disguise"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Requirements"
    desc: "The dragon is wearing their conjured disguise"
  - name: "Effect"
    desc: "The dragon erupts from the disguise, destroying it. The explosive revelation deals 18d6 bludgeoning damage to creatures in a 5-foot emanation with a DC 39 basic Reflex save. A creature that fails its save is [[srd/pf2e/compendium/rules-elements/Conditions#Dazzled|dazzled]] for 1 round as it becomes covered in scraps from the disguise. Any creature sharing a space with the dragon after they erupt is pushed into the nearest empty space."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "When the dragon scores a critical hit with a Strike, they recharge Smoke Breath."
  - name: "Rushed Transformation"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "Using the aid of magic and an exhausting amount of effort, the dragon quickly reshapes their body into the form of a generic [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]] figure. This has the effects of [[srd/pf2e/compendium/spells/rank-2/Humanoid Form|_humanoid form_]] except that it lasts only 1 minute, and the dragon doesn't gain the +4 status bonus to [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] as the transformation makes use of the dragon's body to crudely mimic a humanoid form. The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismiss]] the effect. Whenever the effect ends, the dragon leaves behind scraps of magically conjured flesh, which could give away the dragon's presence."
  - name: "Smoke Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]]) The dragon unleashes a noxious cloud of smoke that deals 16d6 poison damage in a 60-foot cone (DC 39 basic Fortitude save). The smoke remains for 1 minute. This has the effects of [[srd/pf2e/compendium/spells/rank-2/Mist|_mist_]], except it fills the cone's area. The dragon can't use Smoke Breath again for 1d4 rounds."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 3d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] targets."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 41 - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (at will), [[srd/pf2e/compendium/spells/rank-4/Rewrite Memory|Rewrite Memory]] (at will) - __9th__ [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-5/Mind Probe|Mind Probe]], [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (at will), [[srd/pf2e/compendium/spells/rank-4/Rewrite Memory|Rewrite Memory]]"
sourcebook: "_Monster Core_, page 112."
```

```encounter-table
name: Ancient Conspirator Dragon
creatures:
  - 1: Ancient Conspirator Dragon
```

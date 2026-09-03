---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Conspirator Dragon"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/occult
  - pf2e/creature/trait/large
statblock: inline
name: "Young Conspirator Dragon"
level: 8
source: "Monster Core"
aon_id: "creature-2935"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2935"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Conspirator Dragon"
level: "Creature 8"
size: "Large"
trait_01: "Dragon"
trait_02: "Occult"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; (18 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]]) darkvision, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Shadowtongue|Shadowtongue]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +15, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +16, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +18, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +16, [[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +16, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +16, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +18, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +16, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +16"
abilityMods: [5, 3, 2, 2, 4, 4]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +14; __Ref__: +15; __Will__: +18 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Retract Body"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is hit or critically hit by an attack made by a creature the dragon can see"
  - name: "Effect"
    desc: "The dragon retracts the targeted body part or twists away to avoid the attack, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "30 feet, climb 30 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+8 piercing"
  - name: "Melee"
    desc: "⬻ claw +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d6+8 slashing"
  - name: "Melee"
    desc: "⬻ tail +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 1d10+8 bludgeoning"
  - name: "Ranged"
    desc: "⬻ mental blast +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], range 100 feet) __Damage__ 3d6+3 mental"
abilities_bot:
  - name: "Conjure Disguise"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The dragon conjures a perfect flesh-suit replica of a [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] they've seen of their size or smaller and compresses themself into it, along with generating appropriate clothing for the humanoid. This process takes 1 minute to complete, during which the dragon is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. If the dragon stops or is interrupted in this process, the suit is destroyed. Once the process is complete, the dragon can remain in this disguise indefinitely. The transformation has the effects of Change Shape, except that the disguise is not actively magical in nature and doesn't register as [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]] to [[srd/pf2e/compendium/spells/cantrips/detect-magic|_detect magic_]] and similar effects. The dragon loses Retract Body while transformed. If the dragon is critically hit while wearing the disguise, the suit is destroyed and immediately explodes. This has the effects of Detonate Disguise, except that creatures use the outcome one degree of success better than they rolled on their save."
  - name: "Detonate Disguise"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Requirements"
    desc: "The dragon is wearing their conjured disguise"
  - name: "Effect"
    desc: "The dragon erupts from the disguise, destroying it. The explosive revelation deals 9d6 bludgeoning damage to creatures in a 5-foot emanation with a DC 26 basic Reflex save. A creature that fails its save is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round as it becomes covered in scraps from the disguise. Any creature sharing a space with the dragon after they erupt is pushed into the nearest empty space."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "When the dragon scores a critical hit with a Strike, they recharge Smoke Breath."
  - name: "Rushed Transformation"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "Using the aid of magic and an exhausting amount of effort, the dragon quickly reshapes their body into the form of a generic [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] figure. This has the effects of [[srd/pf2e/compendium/spells/rank-2/humanoid-form|_humanoid form_]] except that it lasts only 1 minute, and the dragon doesn't gain the +4 status bonus to [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] as the transformation makes use of the dragon's body to crudely mimic a humanoid form. The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismiss]] the effect. Whenever the effect ends, the dragon leaves behind scraps of magically conjured flesh, which could give away the dragon's presence."
  - name: "Smoke Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The dragon unleashes a noxious cloud of smoke that deals 7d6 poison damage in a 40-foot cone (DC 26 basic Fortitude save). The smoke remains for 1 minute. This has the effects of [[srd/pf2e/compendium/spells/rank-2/mist|_mist_]], except it fills the cone's area. The dragon can't use Smoke Breath again for 1d4 rounds."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] targets."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26 - __1st__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/charm|Charm]], [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]] (at will), [[srd/pf2e/compendium/spells/rank-4/rewrite-memory|Rewrite Memory]]"
sourcebook: "_Monster Core_, page 110."
```

```encounter-table
name: Young Conspirator Dragon
creatures:
  - 1: Young Conspirator Dragon
```

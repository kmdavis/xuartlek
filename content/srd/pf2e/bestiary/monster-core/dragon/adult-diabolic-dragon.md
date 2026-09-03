---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Diabolic Dragon"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Diabolic Dragon"
level: 15
source: "Monster Core"
aon_id: "creature-2939"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2939"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Diabolic Dragon"
level: "Creature 15"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision, scent (imprecise) 60 feet, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +28, Hell Lore +24, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, Legal Lore +26, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +26, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +24, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +27"
abilityMods: [8, 4, 6, 3, 5, 5]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair the dragon's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +29; __Ref__: +25; __Will__: +26 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]"
hp: 285
health:
  - name: "HP"
    desc: "285; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 90 feet, DC 34"
  - name: "Hell's Sting"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]])"
  - name: "Trigger"
    desc: "The dragon is critically hit with a melee attack"
  - name: "Effect"
    desc: "The dragon channels the rancor of [[srd/pf2e/compendium/gm/planes#Hell|Hell]] back through the body of their foe, overwhelming it with an infernal assault on the mind. The triggering creature takes 8d6 mental damage with a DC 36 basic Will save. [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]] creatures use an outcome one degree of success worse than they roll on their saving throw."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "60 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d12+11 piercing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ claws +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d8+11 piercing plus 2d6 fire and Grab"
  - name: "Melee"
    desc: "⬻ tail +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 3d8+11 bludgeoning plus 2d6 fire and Improved Knockdown"
abilities_bot:
  - name: "Diabolic Fire"
    desc: "Any fire damage that a diabolic dragon deals, including fire damage from spells, is imbued with the unholy power of Hell to scorch the spirit as well. A creature takes [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] damage instead of fire damage if that would be more detrimental to the creature (as determined by the GM). A diabolic dragon is immune to the diabolic fire of other diabolic dragons, the fire from [[srd/pf2e/compendium/spells/rank-5/divine-immolation|_divine immolation_]], and similar effects."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hellfire Breath whenever they score a critical hit with a Strike."
  - name: "Hellfire Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) The dragon unleashes a blast of infernal fire that deals 16d6 fire damage in a 50-foot cone (DC 36 basic Reflex save). The dragon can't use Hellfire Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26 - __Cantrips (8th)__ [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]] - __7th__ [[srd/pf2e/compendium/spells/rank-5/divine-immolation|Divine Immolation]], [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (at will; self only), [[srd/pf2e/compendium/spells/rank-4/wall-of-fire|Wall of Fire]] (at will)"
sourcebook: "_Monster Core_, page 113."
```

```encounter-table
name: Adult Diabolic Dragon
creatures:
  - 1: Adult Diabolic Dragon
```

---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Coral Dragon"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/primal
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Coral Dragon"
level: 12
source: "Monster Core 2"
aon_id: "creature-4349"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4349"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Coral Dragon"
level: "Creature 12"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; darkvision, wavesense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +20, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +21, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +18, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +22, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +23"
abilityMods: [7, 2, 5, 3, 5, 7]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +25; __Ref__: +20; __Will__: +21 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Kaleidoscopic Display"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 90 feet. The coral formations covering the dragon's body glow and shimmer with vivid colors, overwhelming the senses and forcing any creature entering or beginning their turn in the aura to attempt a DC 30 Fortitude save. Regardless of the outcome, the creature is temporarily immune to the dragon's kaleidoscopic display for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round."
  - name: "Critical Failure"
    desc: "The creature is blinded for 1 round and dazzled for 1 minute."
  - name: "Reef Bond"
    desc: "Every coral dragon is mystically bound to a single living coral reef. If the dragon moves more than 3 miles from their reef, they become sickened 1 and unable to recover, with the sickened value increasing by 1 every 6 hours unless they succeed at a DC 34 Fortitude save. After 24 hours, the dragon becomes [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]] 1; its drained value increases by 1 every 24 hours. If the dragon's reef suffers significant damage, they immediately become aware of the location where the reef was harmed but not the source or nature of the damage. Should the reef ever be completely destroyed, the dragon is immediately slain."
  - name: "Biomineralize"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by a melee weapon without reach or an unarmed attack that deals slashing or piercing damage"
  - name: "Effect"
    desc: "A gout of blood spurts from the dragon's wound and instantaneously calcifies into a jagged branch of sharpened coral. The coral branch impales the triggering creature, dealing 7d6 piercing damage (DC 32 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). The triggering creature also takes 1d4 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]] on a critical failure. Regardless of the outcome, the coral then crumbles to dust."
speed: "30 feet, fly 50 feet, swim 100"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+13 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+13 slashing"
  - name: "Melee"
    desc: "⬻ tail +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+13 bludgeoning plus Knockdown"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hydraulic Breath whenever they score a critical hit with a Strike."
  - name: "Hydraulic Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]]) The dragon exhales a pressurized jet of water that deals 13d6 bludgeoning damage in an 100-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] (DC 32 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Creatures that critically fail their Reflex save against the Hydraulic Breath are pushed back 10 feet and knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. The dragon can't use Hydraulic Breath again for 1d4 rounds."
  - name: "Reef Meld"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/extradimensional|Extradimensional]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The coral dragon is in physical contact with their bound reef"
  - name: "Effect"
    desc: "The dragon physically merges with the reef and vanishes, along with up to four willing creatures, into an extradimensional space where it can neither affect nor be affected by the outside world. The effect lasts indefinitely or until the dragon Dismisses it. Once merged, the dragon can spend 1 minute traveling to and emerging from any point on its reef up to 5 mile away."
sourcebook: "_Monster Core 2_, page 121."
```

```encounter-table
name: Adult Coral Dragon
creatures:
  - 1: Adult Coral Dragon
```

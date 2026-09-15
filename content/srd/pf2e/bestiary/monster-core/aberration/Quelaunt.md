---
noteType: pf2eMonster
aliases: "Quelaunt"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Quelaunt"
level: 15
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3159"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Quelaunt"
level: "Creature 15"
size: "Large"
trait_01: "Aberration"
modifier: 29
perception:
  - name: "Perception"
    desc: "+29; tremorsense (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]]; (can't speak any language); telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +30, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +27"
abilityMods: [6, 5, 4, 5, 6, 8]
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +27; __Ref__: +26; __Will__: +31 (+33 vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]])"
hp: 305
health:
  - name: "HP"
    desc: "305; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 15"
speed: "40 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Reach|reach 10 feet]]) __Damage__ 3d8+12 slashing"
abilities_bot:
  - name: "Emotional Focus"
    desc: "The quelaunt can cast the following cleric domain spells as 8th-rank occult innate spells at will without spending Focus Points: [[srd/pf2e/compendium/spells/focus/Captivating Adoration|_captivating adoration_]], [[srd/pf2e/compendium/spells/focus/Delusional Pride|_delusional pride_]], and [[srd/pf2e/compendium/spells/focus/Ignite Ambition|_ignite ambition_]]."
  - name: "Emotional Frenzy"
    desc: "⬽ The quelaunt casts up to three spells chosen from its at-will innate spells and its emotional focus spells."
  - name: "Feed on Emotion"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The quelaunt feeds on the emotional unrest of a single creature within 30 feet that's under a harmful [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]] effect. The target must succeed at a DC 37 Will save or take 4d10 mental damage and be [[srd/pf2e/compendium/rules-elements/Conditions#Stunned|stunned]] for 1 round. If the target fails its saving throw, the quelaunt regains the same number of Hit Points and regains the action it spent to Feed on Emotion. It can't use the regained action to Feed on Emotion again."
  - name: "Rapid Strikes"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]]) The quelaunt makes three melee Strikes, each against a different target within reach. The multiple attack penalty applies to each attack but increases only after all the attacks have been made."
  - name: "Spiral of Despair"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]])"
  - name: "Trigger"
    desc: "A creature fails a saving throw to resist one of the quelaunt's innate spells or emotional focus spells"
  - name: "Effect"
    desc: "As the quelaunt invades the triggering creature's mind and plants the seeds of negative emotions, it also strips away the target's feelings of hope or positivity. The quelaunt can immediately end a single [[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]] effect from which the triggering creature is benefiting. Other Quelaunts Perhaps the most frightening tales of quelaunts attribute them with abilities beyond those detailed here, suggesting that quelaunts might be an entire category of alien menace that has only recently turned its awful attention to humanity."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 39 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Laughing Fit|Laughing Fit]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-5/Wave of Despair|Wave of Despair]] (×3) - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/Fly|Fly]]"
sourcebook: "_Monster Core_, page 285."
```

```encounter-table
name: Quelaunt
creatures:
  - 1: Quelaunt
```

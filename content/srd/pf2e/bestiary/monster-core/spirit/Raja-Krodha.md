---
noteType: pf2eMonster
aliases: "Raja-Krodha"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/rakshasa
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Raja-Krodha"
level: 10
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3161"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Raja-Krodha"
level: "Creature 10"
size: "Medium"
trait_01: "Rakshasa"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/Languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +21, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +19, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +18, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +23"
abilityMods: [6, 6, 4, 2, 2, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] taravari_ (functions as a [[srd/pf2e/compendium/equipment/weapons/sword/Scimitar|scimitar]])"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +20; __Will__: +18 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 180
health:
  - name: "HP"
    desc: "180; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 10, Immunities [[srd/pf2e/compendium/rules-elements/traits/player-core/Fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]]"
abilities_mid:
  - name: "Knowledge of Delusion"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]]) A creature that fails a [[srd/pf2e/compendium/rules-elements/actions/player-core#Recall Knowledge|Recall Knowledge]] check or a Perception check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]] on a rakshasa is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] until the end of its next turn."
  - name: "Reassert Fate"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]])"
  - name: "Trigger"
    desc: "A creature within 30 feet uses a [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]] effect"
  - name: "Effect"
    desc: "The raja-krodha reasserts the ebb and flow of fate, instilling a deep dread in those who would attempt to cheat their written role. They disrupt the triggering effect, and the triggering creature becomes [[srd/pf2e/compendium/rules-elements/Conditions#Frightened|frightened 2]] and is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the raja-krodha until the end of its next turn."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ taravari +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+12 slashing"
  - name: "Melee"
    desc: "⬻ fangs +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d6+12 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d4+12 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The raja-krodha takes on the appearance of any Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't change the raja-krodha's Speed or their attack and damage modifiers with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). They lose their fangs Strike unless the humanoid form has fangs or a similar unarmed attack."
  - name: "Cruel Majesty"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Visual|Visual]])"
  - name: "Requirements"
    desc: "The rakshasa is not in its true form"
  - name: "Effect"
    desc: "The rakshasa Changes Shape into its true form in a display that is equal parts terrifying and majestic. Creatures within 30 feet of the rakshasa must succeed at a DC 29 Will save or be [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] to the rakshasa until the beginning of the rakshasa's next turn as they are awestruck."
  - name: "Sneak Attack"
    desc: "The raja-krodha deals 2d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
  - name: "Swallow Whole"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Attack|Attack]]) Medium, 2d12+6 bludgeoning, Rupture 15"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Divine Lance|Divine Lance]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Clairaudience|Clairaudience]], [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Clairvoyance|Clairvoyance]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]], [[srd/pf2e/compendium/spells/rank-3/Vampiric Feast|Vampiric Feast]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/Crisis of Faith|Crisis of Faith]], [[srd/pf2e/compendium/spells/rank-5/Hallucination|Hallucination]], [[srd/pf2e/compendium/spells/rank-5/Invoke Spirits|Invoke Spirits]] __Cleric Domain Spells (2 Focus Points),__ DC 29 - __5th__ [[srd/pf2e/compendium/spells/focus/Ignite Ambition|Ignite Ambition]], [[srd/pf2e/compendium/spells/focus/Savor the Sting|Savor the Sting]]"
sourcebook: "_Monster Core_, page 287."
```

```encounter-table
name: Raja-Krodha
creatures:
  - 1: Raja-Krodha
```

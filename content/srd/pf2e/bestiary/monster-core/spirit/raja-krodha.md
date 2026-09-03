---
obsidianUIMode: preview
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
aon_id: "creature-3161"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3161"
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
    desc: "Perception +18; darkvision"
languages: "Chthonian, Common, Diabolic, Empyrean, Sakvroth"
skills:
  - name: "Skills"
    desc: "Athletics +19, Deception +21, Diplomacy +21, Intimidation +21, Performance +19, Religion +18, Stealth +23"
abilityMods: [6, 6, 4, 2, 2, 5]
abilities_top:
  - name: "Items"
    desc: "_+1 striking taravari_ (functions as a scimitar)"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +20; __Will__: +18 +2 status to all saves vs. magic"
hp: 180
health:
  - name: "HP"
    desc: "180; __Weaknesses__ holy 10, Immunities fear, fortune, misfortune"
abilities_mid:
  - name: "Knowledge of Delusion"
    desc: "(divine) A creature that fails a Recall Knowledge check or a Perception check to Sense Motive on a rakshasa is off-guard until the end of its next turn."
  - name: "Reassert Fate"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "A creature within 30 feet uses a fortune or misfortune effect"
  - name: "Effect"
    desc: "The raja-krodha reasserts the ebb and flow of fate, instilling a deep dread in those who would attempt to cheat their written role. They disrupt the triggering effect, and the triggering creature becomes frightened 2 and is off-guard to the raja-krodha until the end of its next turn."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ taravari +23 (Forceful, Magical, Sweep, Unholy) __Damage__ 2d6+12 slashing"
  - name: "Melee"
    desc: "⬻ fangs +20 (Agile, Magical, Unholy) __Damage__ 2d6+12 piercing plus Grab"
  - name: "Melee"
    desc: "⬻ claw +22 (Agile, Finesse, Magical, Unholy) __Damage__ 2d4+12 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The raja-krodha takes on the appearance of any Medium humanoid. This doesn't change the raja-krodha's Speed or their attack and damage modifiers with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning). They lose their fangs Strike unless the humanoid form has fangs or a similar unarmed attack."
  - name: "Cruel Majesty"
    desc: "⬻ (Emotion, Mental, Visual)"
  - name: "Requirements"
    desc: "The rakshasa is not in its true form"
  - name: "Effect"
    desc: "The rakshasa Changes Shape into its true form in a display that is equal parts terrifying and majestic. Creatures within 30 feet of the rakshasa must succeed at a DC 29 Will save or be off-guard to the rakshasa until the beginning of the rakshasa's next turn as they are awestruck."
  - name: "Sneak Attack"
    desc: "The raja-krodha deals 2d6 extra precision damage to off-guard creatures."
  - name: "Swallow Whole"
    desc: "⬻ (Attack) Medium, 2d12+6 bludgeoning, Rupture 15"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29 - __Cantrips (5th)__ Detect Magic, Divine Lance - __2nd__ Invisibility - __3rd__ Clairaudience, Haste - __4th__ Clairvoyance, Unfettered Movement, Vampiric Feast - __5th__ Crisis of Faith, Hallucination, Invoke Spirits __Cleric Domain Spells (2 Focus Points),__ DC 29 - __5th__ Ignite Ambition, Savor the Sting"
sourcebook: "_Monster Core_, page 287."
```

```encounter-table
name: Raja-Krodha
creatures:
  - 1: Raja-Krodha
```

---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Succubus"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Succubus"
level: 7
source: "Monster Core"
aon_id: "creature-2897"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2897"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Succubus"
level: "Creature 7"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Chthonian, Common, Draconic, Empyrean; three additional mortal languages, telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Deception +18, Diplomacy +20, Intimidation +16, Religion +13, Society +15, Stealth +14"
abilityMods: [2, 3, 4, 4, 2, 7]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +14; __Will__: +17 +1 status to all saves vs. magic"
hp: 100
health:
  - name: "HP"
    desc: "100; __Weaknesses__ cold iron 5, holy 5"
abilities_mid:
  - name: "Seductive Presence"
    desc: "(aura, emotion, mental) 10 feet. Any creature in the aura that could be sexually attracted to a succubus takes a –2 circumstance penalty to checks and DCs to oppose the succubus's mental spells, Deception, and Diplomacy."
  - name: "Rejection Vulnerability"
    desc: "As succubi are beings of pure lust, creatures that reject their lust can metaphysically harm them. When a succubus fails a Diplomacy check to Embrace or Request, or when a creature succeeds at its save against a succubus's mental spell or ability, the succubus takes 2d6 mental damage. For 1 hour after causing mental damage to a succubus in this way, a creature can deal 2d6 mental damage to the succubus with a successful Demoralize action incorporating its rejection."
speed: "25 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +16 (Agile, Finesse, Magical, Unholy) __Damage__ 2d8+8 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Divine, Polymorph) The succubus can take on the appearance of any Small or Medium humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Embrace"
    desc: "⬻ The succubus attempts to Grapple a creature using their Diplomacy bonus instead of Athletics. If the creature is willing, the succubus automatically succeeds."
  - name: "Passionate Kiss"
    desc: "⬻ (Divine, Emotion, Mental, Unholy, Void)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The succubus engages a creature they have grabbed or restrained in an embrace or other act of passion to drain its vital essence. The kiss makes the creature drained 1 or increases its drained value by 1, to a maximum of 4. The creature takes 3d6 void damage and the succubus regains Hit Points equal to the damage dealt. The target must succeed at a DC 26 Will save or be affected by a _suggestion_ to submit to more actions of passion rather than trying to Escape."
  - name: "Profane Gift"
    desc: "⬽ (Divine, Mental, Unholy)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The succubus gives a willing humanoid a profane gift. That creature gains a +1 status bonus to attack rolls, skill checks, and saving throws. As long as the gift persists, the succubus can communicate telepathically with the target at any distance, see through the creature's senses, and target the creature with _suggestion_ through the telepathic link. In addition, the creature uses an outcome one degree of success worse than it rolls on saving throws against the succubus's _suggestion_ spells. A humanoid can't have more than one profane gift at a time, and a succubus can't grant more than one profane gift at a time. Removing the gift requires an _atone_ ritual. The succubus can remove the gift as a free action to give the recipient a curse, making them stupefied 3 with an unlimited duration. A summoned succubus can't grant a profane gift."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __1st__ Charm (at will) - __3rd__ Mind Reading (at will) - __4th__ Translocate (at will), Suggestion (at will) - __5th__ Translocate - __6th__ Dominate - __Constant (5th)__ Truespeech"
  - name: "Rituals"
    desc: "DC 26 - __1st__ Demonic Pact"
sourcebook: "_Monster Core_, page 78."
```

```encounter-table
name: Succubus
creatures:
  - 1: Succubus
```

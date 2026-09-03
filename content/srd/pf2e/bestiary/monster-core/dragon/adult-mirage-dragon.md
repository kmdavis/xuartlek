---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Mirage Dragon"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Mirage Dragon"
level: 13
source: "Monster Core"
aon_id: "creature-2951"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2951"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Adult Mirage Dragon"
level: "Creature 13"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, illusion sense, scent (imprecise) 60 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +24, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +24, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +29, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +27, Illusion Lore +26, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +25"
abilityMods: [6, 6, 5, 5, 6, 8]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Hide|Hide]] in natural environments even if they don't have cover."
  - name: "Illusion Sense"
    desc: "When the dragon moves within 30 feet of an [[srd/pf2e/compendium/rules-elements/traits/player-core/illusion|illusion]] that can be disbelieved, they automatically attempt a [[srd/pf2e/compendium/rules-elements/traits/player-core/secret|secret]] check to disbelieve, even if they didn't spend an action to Interact."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +23; __Will__: +25 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]]"
hp: 235
health:
  - name: "HP"
    desc: "235; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Scintillating Defense"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "The dragon flashes their iridescent scales at the triggering creature to throw off the attack. The dragon gains [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]]against the triggering attack."
speed: "50 feet, climb 30 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+12 piercing"
  - name: "Melee"
    desc: "⬻ claws +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+12 slashing"
  - name: "Melee"
    desc: "⬻ tail +23 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+12 bludgeoning"
abilities_bot:
  - name: "Captivating Display"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]])"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The dragon opens the fins on their head, creating a radiant display of enthralling colors. Each creature in a 30-foot emanation must succeed at a DC 33 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] and [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] (or slowed 2 on a critical failure) for 1 round. Regardless of the result, a creature is then temporarily immune to Captivating Display for 1 minute."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hallucinatory Breath whenever they score a critical hit with a Strike."
  - name: "Hallucinatory Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]]) The dragon breathes a cloud that assaults the senses and deals 12d6 mental damage in a 40-foot cone (DC 33 Will save). A creature that fails its save is also [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] for 1 round (1 minute on a critical failure) and is then temporarily immune to being confused by Hallucinatory Breath for 1 hour. The dragon can't use Hallucinatory Breath again for 1d4 rounds."
  - name: "Lunging Bite"
    desc: "⬺ The dragon lunges their head forward, making a jaws Strike with an extended reach of 25 feet."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 2d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] targets."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 35 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/message|Message]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/illusory-object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] - __6th__ [[srd/pf2e/compendium/spells/rank-2/illusory-creature|Illusory Creature]], [[srd/pf2e/compendium/spells/rank-5/illusory-scene|Illusory Scene]], [[srd/pf2e/compendium/spells/rank-4/mirage|Mirage]], [[srd/pf2e/compendium/spells/rank-6/vibrant-pattern|Vibrant Pattern]]"
sourcebook: "_Monster Core_, page 122."
```

```encounter-table
name: Adult Mirage Dragon
creatures:
  - 1: Adult Mirage Dragon
```

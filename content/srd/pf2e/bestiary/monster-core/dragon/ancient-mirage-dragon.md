---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Mirage Dragon"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Ancient Mirage Dragon"
level: 18
source: "Monster Core"
aon_id: "creature-2952"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2952"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ancient Mirage Dragon"
level: "Creature 18"
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 33
perception:
  - name: "Perception"
    desc: "Perception +33; darkvision, illusion sense, scent (imprecise) 60 feet"
languages: "Common, Draconic, Fey, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Arcana +32, Athletics +34, Crafting +32, Deception +37, Diplomacy +35, Illusion Lore +34, Performance +35, Stealth +35, Thievery +33"
abilityMods: [7, 7, 6, 6, 7, 9]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can Hide in natural environments even if they don't have cover."
  - name: "Illusion Sense"
    desc: "When the dragon moves within 30 feet of an illusion that can be disbelieved, they automatically attempt a secret check to disbelieve, even if they didn't spend an action to Interact."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +28; __Ref__: +29; __Will__: +33 +2 status to all saves vs. arcane"
hp: 345
health:
  - name: "HP"
    desc: "345; __Immunities__ fascinated, paralyzed, sleep"
abilities_mid:
  - name: "Scintillating Defense"
    desc: "⬲ (visual)"
  - name: "Trigger"
    desc: "The dragon is targeted with an attack"
  - name: "Effect"
    desc: "The dragon flashes their iridescent scales at the triggering creature to throw off the attack. The dragon gains concealmentagainst the triggering attack."
speed: "60 feet, climb 40 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 (Magical, reach 15 feet) __Damage__ 3d10+15 piercing"
  - name: "Melee"
    desc: "⬻ claws +33 (Agile, Magical, reach 10 feet) __Damage__ 3d6+15 slashing"
  - name: "Melee"
    desc: "⬻ tail +31 (Magical, reach 20 feet) __Damage__ 3d8+15 bludgeoning"
abilities_bot:
  - name: "Captivating Display"
    desc: "⬻ (Arcane, Visual)"
  - name: "Frequency"
    desc: "once per 10 minutes"
  - name: "Effect"
    desc: "The dragon opens the fins on their head, creating a radiant display of enthralling colors. Each creature in a 30-foot emanation must succeed at a DC 41 Will save or be dazzled and slowed 1 (or slowed 2 on a critical failure) for 1 round. Regardless of the result, a creature is then temporarily immune to Captivating Display for 1 minute."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Hallucinatory Breath whenever they score a critical hit with a Strike."
  - name: "Hallucinatory Breath"
    desc: "⬺ (Arcane, Emotion, Mental) The dragon breathes a cloud that assaults the senses and deals 17d6 mental damage in a 50-foot cone (DC 41 Will save). A creature that fails its save is also confused for 1 round (1 minute on a critical failure) and is then temporarily immune to being confused by Hallucinatory Breath for 1 hour. The dragon can't use Hallucinatory Breath again for 1d4 rounds."
  - name: "Lunging Bite"
    desc: "⬺ The dragon lunges their head forward, making a jaws Strike with an extended reach of 25 feet."
  - name: "Sneak Attack"
    desc: "The dragon's Strikes deal an additional 3d6 precision damage to off-guard targets."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 43 - __Cantrips (9th)__ Figment, Message - __4th__ Invisibility (at will) - __8th__ Illusory Creature, Illusory Object (at will), Illusory Scene (at will), Mirage, Vibrant Pattern"
sourcebook: "_Monster Core_, page 123."
```

```encounter-table
name: Ancient Mirage Dragon
creatures:
  - 1: Ancient Mirage Dragon
```

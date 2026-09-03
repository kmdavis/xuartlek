---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ostiarius"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Ostiarius"
level: 5
source: "Monster Core 2"
aon_id: "creature-4607"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4607"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ostiarius"
level: "Creature 5"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; greater darkvision, painsight, sense portal"
languages: "Common, Diabolic, Shadowtongue; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Deception +12, Diplomacy +12, Intimidation +16, Religion +11, Torture Lore +11"
abilityMods: [0, 4, 2, 2, 4, 5]
abilities_top:
  - name: "Painsight"
    desc: "(divine) A velstrac automatically knows whether a creature it sees has any of the doomed, dying, and wounded conditions as well as the value of those conditions."
  - name: "Sense Portal"
    desc: "(divine) The ostiarius always knows the direction and distance to the closest portal between the Netherworld and the Universe. This sense functions only on these two planes."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +15; __Will__: +13 +1 status to all saves vs. magic"
hp: 65
health:
  - name: "HP"
    desc: "65 , regeneration 5 (deactivated by holy or silver); __Immunities__ cold; __Weaknesses__ holy 5, silver 5"
abilities_mid:
  - name: "Whispering Wounds"
    desc: "(aura, divine, mental, visual) 30 feet. When a creature ends its turn in the aura, it hears the wounds on the ostiarius's body whisper obscene truths. The creature must succeed at a DC 21 Will save or become sickened 1."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 (Agile, finesse, magical, unholy) __Damage__ 2d6+2 slashing plus 2d6 persistent bleed"
abilities_bot:
  - name: "Compel Courage"
    desc: "⬻ (Auditory, divine, emotion, linguistic, mental) The ostiarius inspires their willing allies and themself by whispering words of courage from their wounds. The ostiarius and their allies in a 50-foot emanation gain a +1 status bonus to attack rolls, damage rolls, and saves against fear effects. The ostiarius can Sustain Compel Courage. Non-velstracs who accept this compelled courage find bleeding wounds opening on their own bodies to whisper in thanks. They take 1 persistent bleed damage and can't attempt a flat check to end this damage as long as they're compelled."
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, mental, visual) The ostiarius stares at a creature they can see within 30 feet. The creature must immediately attempt a Will save against whispering wounds. In addition, if the creature was already sickened and fails its save, the creature is fascinated by the ostiarius and can't use hostile actions. This fascination lasts for 1 round or until the ostiarius takes any hostile action against the creature or the creature's allies. Whether the creature succeeds at or fails the save, it's temporarily immune to Focus Gaze for 1 hour."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24 - __Cantrips (3rd)__ Shield - __2nd__ Calm (at will), Darkness, Silence - __3rd__ Enthrall, Safe Passage"
  - name: "Rituals"
    desc: "DC 22 - __2nd__ Inveigle"
sourcebook: "_Monster Core 2_, page 345."
```

```encounter-table
name: Ostiarius
creatures:
  - 1: Ostiarius
```

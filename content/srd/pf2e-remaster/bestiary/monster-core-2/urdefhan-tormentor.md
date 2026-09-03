---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Urdefhan Tormentor"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/urdefhan
  - pf2e/creature/trait/medium
statblock: inline
name: "Urdefhan Tormentor"
level: 5
source: "Monster Core 2"
aon_id: "creature-4600"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4600"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Urdefhan Tormentor"
level: "Creature 5"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Unholy"
trait_03: "Urdefhan"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; greater darkvision"
languages: "Aklo, Daemonic, Sakvroth"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Crafting +9, Intimidation +11, Occultism +12, Religion +13"
abilityMods: [3, 1, 3, 2, 4, 2]
abilities_top:
  - name: "Items"
    desc: "Warhammer"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +10; __Will__: +15"
hp: 75
health:
  - name: "HP"
    desc: "75 (void healing); __Immunities__ death effects, disease, fear; __Weaknesses__ vitality 5 Necrotic Decay (divine, void) When an urdefhan dies, their translucent flesh quickly rots away and sublimates into a foul-smelling gas that fills a 5-foot emanation around the body. This gas deals 5d6 void damage to creatures in this area as their flesh curdles and rots (DC 21 basic Fortitude save)."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ warhammer +12 (Shove) __Damage__ 1d8+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ jaws +14 __Damage__ 2d6+5 piercing plus Wicked Bite"
abilities_bot:
  - name: "Stoke the Fervent"
    desc: "⬺ (Auditory, divine, emotion, mental)"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The urdefhan lets out a battle cry, sending themself and their allies into a fanatical frenzy. The tormentor and each ally that hears the call gains a +1 status bonus to attack rolls, damage rolls, and saving throws, and takes a –1 status penalty to AC. Affected creatures must use at least one of their actions to Strike each round, if they're able (even if it means attacking an ally, object, or thin air). This lasts for 2d4 rounds."
  - name: "Wicked Bite"
    desc: "⬻"
  - name: "Requirements"
    desc: "The urdefhan damaged a creature with a jaws Strike on their last action"
  - name: "Effect"
    desc: "The urdefhan maintains contact, turning the creature's flesh translucent around the site of the injury. The target must succeed at a DC 22 Fortitude save or be affected by drain blood or drain vitality (the urdefhan's choice). If the jaws Strike was a critical hit, the creature is affected by both effects, using the same save result for both."
  - name: "Drain Blood"
    desc: "The urdefhan drinks some of the creature's blood. On a failed save, the creature is drained 1 and the urdefhan regains 5 HP (or, on a critical failure, it's drained 2 and the urdefhan regains 10 HP)."
  - name: "Drain Vitality"
    desc: "The urdefhan draws out some of the creature's vital essence. The creature becomes enfeebled 1 for 1 hour on a failed save (or enfeebled 2 for 1 hour on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23 - __1st__ Enfeeble, Gentle Landing (self only), Grim Tendrils, Harm - __2nd__ Darkness, False Vitality, Harm, See the Unseen - __3rd__ Harm, Paralyze"
  - name: "Rituals"
    desc: "DC 23 - __1st__ Daemonic Pact"
sourcebook: "_Monster Core 2_, page 337."
```

```encounter-table
name: Urdefhan Tormentor
creatures:
  - 1: Urdefhan Tormentor
```

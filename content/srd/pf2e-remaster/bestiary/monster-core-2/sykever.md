---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sykever"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/darvakka
  - pf2e/creature/trait/shadow
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Sykever"
level: 15
source: "Monster Core 2"
aon_id: "creature-4311"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4311"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sykever"
level: "Creature 15"
size: "Huge"
trait_01: "Darvakka"
trait_02: "Shadow"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; greater darkvision, lifesense 60 feet"
languages: "Chthonian, Common, Diabolic, Necril; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Arcana +27, Athletics +29, Intimidation +28, Netherworld Lore +27, Religion +27, Stealth +27, Void Lore +27, Warfare Lore +27"
abilityMods: [8, 4, 6, 6, 6, 7]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +25; __Ref__: +25; __Will__: +31"
hp: 310
health:
  - name: "HP"
    desc: "310 (void healing); __Immunities__ bleed, death effects, disease, paralyzed, poison, unconscious; __Resistances__ cold 10; __Weaknesses__ holy 10, silver 10"
abilities_mid:
  - name: "Entropy's Shadow"
    desc: "(aura, divine, void) 40 feet. Darvakkas leak entropy and corruption from their very being. A living creature entering or starting its turn in the aura takes 4d6 void damage with a DC 33 basic Fortitude save. If it fails, it's also enfeebled 1 for 1 minute and pulled 10 feet toward the darvakka."
  - name: "Sunlight Powerlessness"
    desc: "A darvakka caught in sunlight is stunned 2 and clumsy 2 as long as it remains in the sunlight."
speed: "40 feet; fly"
attacks:
  - name: "Melee"
    desc: "⬻ horn +31 (Magical, reach 10 feet) __Damage__ 3d8+12 bludgeoning plus 1d10 cold and 2d8 persistent bleed"
  - name: "Melee"
    desc: "⬻ arm spike +31 (Agile, magical, reach 10 feet) __Damage__ 3d8+12 piercing plus 1d10 cold"
abilities_bot:
  - name: "Change Posture"
    desc: "⬻ The sykever changes between their bipedal and quadrupedal stance. In their bipedal stance, the sykever can use all the abilities in their stat block except Horned Rush. In their quadrupedal stance, the sykever has a Speed of 80 feet but can't make arm spike Strikes, Disarm, cast spells, or use Crush Item."
  - name: "Crush Item"
    desc: "⬲"
  - name: "Trigger"
    desc: "The sykever gets a critical success to Disarm"
  - name: "Requirements"
    desc: "The sykever is in their bipedal stance"
  - name: "Effect"
    desc: "The sykever snatches the item and pierces it with their arm spikes. The item becomes broken and falls to the ground in the sykever's space. Items that are already broken aren't further damaged, and an item with 14 or higher Hardness is unaffected."
  - name: "Draining Gaze"
    desc: "⬻ (Concentrate, divine, visual) The sykever fixes their nightmarish gaze on one creature they can see, who must attempt a DC 36 Will save. Regardless of the result, the target is temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is enfeebled 2 for 1 round if the sykever is in bipedal stance or clumsy 2 for 1 round if the sykever is in quadrupedal stance."
  - name: "Failure"
    desc: "As success, but the effect lasts 1 minute."
  - name: "Critical Failure"
    desc: "As success, but enfeebled 3 or clumsy 3, and the effect lasts 10 minutes."
  - name: "Horned Rush"
    desc: "⬻"
  - name: "Requirements"
    desc: "The sykever is in their quadrupedal stance"
  - name: "Effect"
    desc: "The sykever Strides and then makes a horn Strike. The Bound One Hidden beneath the necromantic colleges of Yled in the nation of Geb are a trio of sykevers held in magical stasis alongside an ancient darvakka known only as the Bound One. This creature, ensnared by Geb himself, serves as an unending pool of void energy, immensely useful for magical experiments and empowering other undead servitors around the nation. The four darvakkas await the day Geb calls upon them once more."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36 - __Cantrips (8th)__ Detect Magic - __4th__ Darkness (at will), Invisibility (×3) - __6th__ Truesight - __7th__ Harm (×3), Interplanar Teleport (to the Universe; the Void; or the Netherworld only), Paralyze - __Constant (8th)__ Fly"
sourcebook: "_Monster Core 2_, page 85."
```

```encounter-table
name: Sykever
creatures:
  - 1: Sykever
```

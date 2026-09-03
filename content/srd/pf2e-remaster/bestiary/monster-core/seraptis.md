---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Seraptis"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Seraptis"
level: 15
source: "Monster Core"
aon_id: "creature-2899"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2899"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Seraptis"
level: "Creature 15"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, _truesight_"
languages: "Chthonian, Draconic, Empyrean; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +31, Deception +29, Religion +27, Stealth +28"
abilityMods: [8, 7, 6, 3, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+1 striking wounding scimitar_ (2)"
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +27; __Ref__: +28; __Will__: +25 +1 status to all saves vs. magic"
hp: 340
health:
  - name: "HP"
    desc: "340; __Weaknesses__ cold iron 15, holy 15"
abilities_mid:
  - name: "Blood Healing"
    desc: "(aura, healing, vitality) 30 feet. Whenever a humanoid within the aura takes bleed damage, the blood flows through the air to the seraptis's mouths and the seraptis heals by the same amount."
  - name: "Recovery Vulnerability"
    desc: "When a creature within the seraptis's blood healing aura recovers from persistent damage, the seraptis takes 3d6 mental damage."
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _wounding scimitar_ +32 (Forceful, Magical, Sweep, Unholy) __Damage__ 2d6+16 slashing plus 2d6 mental and 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +31 (Agile, Magical, Unholy) __Damage__ 2d4+16 slashing plus 2d6 mental and Grab"
  - name: "Ranged"
    desc: "⬻ caustic blood +30 (Acid, Magical, Unholy) __Damage__ 7d6 acid"
abilities_bot:
  - name: "Bloody Dance"
    desc: "⬺ The seraptis makes a Strike with up to four arms, each against a different target and using a claw or scimitar as appropriate. These attacks count toward the seraptis's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks. The seraptis can use Grab following this activity, separately attempting to Grapple each creature hit by a claw."
  - name: "Gnawing Arms"
    desc: "⬻ (Unholy)"
  - name: "Requirements"
    desc: "The seraptis has at least one creature grabbed or restrained"
  - name: "Effects"
    desc: "The seraptis's arm mouths gnaw on those creatures, dealing each of them 2d6+8 piercing damage with a DC 37 basic Fortitude save. Creatures that fail the save also take 2d6 persistent bleed damage."
  - name: "Isolating Words"
    desc: "⬻ (Mental, Curse, Linguistic) The seraptis telepathically explains a plausible secret to a creature within 30 feet. That creature must succeed at a DC 37 Will save or be mentally cut off from those around them for 1 minute (or permanently on a critical failure). The affected creature treats no one as an ally and any speech they hear is warped, encouraging conflict, and negating any linguistic ability from creatures that aren't unholy. Regardless of the results of the saving throw, the creature is immune to Isolating Words for 24 hours."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 35 - __3rd__ Illusory Disguise (at will) - __4th__ Translocate (at will) - __5th__ Translocate - __8th__ Dominate, Phantasmal Calamity, Wave of Despair - __Constant (8th)__ Truesight, Truespeech"
  - name: "Rituals"
    desc: "DC 36 - __1st__ Demonic Pact"
sourcebook: "_Monster Core_, page 80."
```

```encounter-table
name: Seraptis
creatures:
  - 1: Seraptis
```

---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Yamah"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/azata
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Yamah"
level: 5
source: "Monster Core 2"
aon_id: "creature-4093"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4093"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Yamah"
level: "Creature 5"
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, _detect magic_"
languages: "Diabolic, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Arcana +10, Deception +12, Diplomacy +12, Religion +13, Stealth +13"
abilityMods: [3, 4, 2, 3, 4, 5]
abilities_top:
  - name: "Items"
    desc: "Starknife, _forceful quartz bracelet_ with 3 gems"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +13; __Will__: +13"
hp: 75
health:
  - name: "HP"
    desc: "75; __Weaknesses__ cold iron 5, unholy 5"
abilities_mid:
  - name: "Free Mind"
    desc: "⬲ (mental)"
  - name: "Trigger"
    desc: "An ally of the yamah's attempts a saving throw against an effect that has the mental trait"
  - name: "Effect"
    desc: "The ally's gains a +4 status bonus to the saving throw. If the ally rolls a success, they get a critical success instead."
speed: "25 feet, fly 70 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _starknife_ +15 (Agile, deadly d6, Finesse, Holy, Magical, thrown 20 feet, versatile S) __Damage__ 2d4+8 piercing"
  - name: "Ranged"
    desc: "⬻ _starknife_ +15 (Agile, deadly d6, Finesse, Holy, Magical, thrown 20 feet, versatile S) __Damage__ 2d4+8 piercing"
abilities_bot:
  - name: "Crystallized Attack"
    desc: "⭓ (Divine, Manipulate)"
  - name: "Requirements"
    desc: "The yamah has a charged gem on its _forceful quartz bracelet_"
  - name: "Effect"
    desc: "The yamah channels the magic from an active gem, causing its starknife to glow with unnatural brightness. Their next starknife Strike before the end of their turn deals an extra 1d6 force damage and increases its thrown range to 60 feet. This drains one of their quartz gems."
  - name: "Sneak Attack"
    desc: "The yamah's Strikes deal an extra 1d6 precision damage to off-guard creatures."
  - name: "Starstrike"
    desc: "Any non-magical starknife becomes a _+1 striking returning weapon_ while a yamah wields it."
  - name: "Steal Magic"
    desc: "⬺ (Concentrate, Divine) The yamah makes a melee spell attack against a creature under the effects of a spell; a yamah automatically succeeds with this attack against a willing creature. On a success, the yamah's divine touch attempts to counteract the spell (counteract rank 3, counteract modifier +16). A successful counteract siphons the magical energy into one of the gems on its _forceful quartz bracelet_, recharging it. Yamah Bracelets Each yamah wears a personalized bracelet, embedded with quartz gems that reflect the cosmos. These are empowered by unseen magic, recharging when the yamah has 8 hours of rest. These bracelets have a unique divine connection to their respective yamah, and the bracelets only function for that yamah. On occasion, a yamah will gift the bracelet to a mortal, more as a symbol of trust and a sign that the individual is protected than an attempt to share power."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +14 - __Cantrips (3rd)__ Divine Lance - __2nd__ Heal (×2), Invisibility, Sure Footing - __3rd__ Holy Light, Dispel Magic - __Constant (5th)__ Detect Magic, Truespeech"
sourcebook: "_Monster Core 2_, page 50."
```

```encounter-table
name: Yamah
creatures:
  - 1: Yamah
```

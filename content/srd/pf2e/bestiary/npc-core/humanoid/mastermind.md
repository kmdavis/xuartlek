---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mastermind"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Mastermind"
level: 4
source: "NPC Core"
aon_id: "creature-3612"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3612"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mastermind"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; (17 to Sense Motive)"
languages: "Common; two additional languages"
skills:
  - name: "Skills"
    desc: "Arcana +13, Deception +15, Diplomacy +15, Intimidation +15, Occultism +15, Performance +17, Religion +11, Society +17, Stealth +11, Thievery +9, Underworld Lore +17"
abilityMods: [0, 3, 0, 4, 2, 4]
abilities_top:
  - name: "Manipulation Specialist"
    desc: "When competing in a social or intellectual arena, the mastermind is a 7th-level challenge."
  - name: "Versatile Performance"
    desc: "The mastermind can use Performance instead of Diplomacy to Make an Impression and instead of Deception to Impersonate."
  - name: "Items"
    desc: "Disguise Kit, Hand Crossbow (10 bolts), Leather Armor, Shortsword"
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +6; __Ref__: +11; __Will__: +16"
hp: 55
health:
  - name: "HP"
    desc: "55"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +13 (Agile, Finesse, versatile S) __Damage__ 1d6+6 slashing"
  - name: "Melee"
    desc: "⬻ fist +13 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +13 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 22 - __Cantrips (2nd)__ Courageous Anthem, Uplifting Overture"
  - name: "Scoundrel's Feint"
    desc: "When the mastermind successfully Feints, the target is off-guard against the mastermind's melee attacks until the end of the mastermind's next turn. On a critical success, the target is off-guard against all melee attacks for that time, not just the mastermind's."
  - name: "Sneak Attack"
    desc: "The mastermind deals an extra 1d6 precision damage to off-guard creatures."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (2nd)__ Daze, Detect Magic, Message, Prestidigitation, Sigil - __1st__ Charm, Illusory Disguise, Illusory Object (3 slots) - __2nd__ Blur, Charm, Invisibility, Paranoia (3 slots)"
sourcebook: "_NPC Core_, page 156."
```

```encounter-table
name: Mastermind
creatures:
  - 1: Mastermind
```

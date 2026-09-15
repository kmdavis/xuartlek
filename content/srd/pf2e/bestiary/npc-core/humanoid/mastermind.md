---
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
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3612"
socialImage: og-image.png
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
    desc: "+10; (17 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]; two additional languages"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +15, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +17, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +11, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/Thievery|Thievery]] +9, [[srd/pf2e/compendium/rules-elements/skills/Lore|Underworld Lore]] +17"
abilityMods: [0, 3, 0, 4, 2, 4]
abilities_top:
  - name: "Manipulation Specialist"
    desc: "When competing in a social or intellectual arena, the mastermind is a 7th-level challenge."
  - name: "Versatile Performance"
    desc: "The mastermind can use [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] instead of [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Make an Impression|Make an Impression]] and instead of [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] to [[srd/pf2e/compendium/rules-elements/actions/player-core#Impersonate|Impersonate]]."
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
    desc: "⬻ shortsword +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+6 slashing"
  - name: "Melee"
    desc: "⬻ fist +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ hand crossbow +13 (range increment 60 feet, reload 1) __Damage__ 1d6+6 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 22 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Uplifting Overture|Uplifting Overture]]"
  - name: "Scoundrel's Feint"
    desc: "When the mastermind successfully [[srd/pf2e/compendium/rules-elements/actions/player-core#Feint|Feints]], the target is [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] against the mastermind's melee attacks until the end of the mastermind's next turn. On a critical success, the target is off-guard against all melee attacks for that time, not just the mastermind's."
  - name: "Sneak Attack"
    desc: "The mastermind deals an extra 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/Conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Sigil|Sigil]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]], [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]] (3 slots)"
sourcebook: "_NPC Core_, page 156."
```

```encounter-table
name: Mastermind
creatures:
  - 1: Mastermind
```

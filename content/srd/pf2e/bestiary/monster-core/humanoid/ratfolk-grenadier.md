---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ratfolk Grenadier"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/ratfolk
  - pf2e/creature/trait/medium
statblock: inline
name: "Ratfolk Grenadier"
level: 4
source: "Monster Core"
aon_id: "creature-3164"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3164"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Ratfolk Grenadier"
level: "Creature 4"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Ratfolk"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Ysoki|Ysoki]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +9, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +9"
abilityMods: [0, 4, 2, 4, 2, 1]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "The grenadier carries 6 alchemical grenades that deal either acid, cold, or fire damage plus 2 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent damage]] and 2 [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage of the same type (typically two of each). The grenadier replenishes these each day using scavenged materials."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/alchemists-toolkit|Alchemist's Toolkit]], Hand Crossbow (20 bolts), Studded Leather Armor"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +13; __Will__: +9"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +12 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4 piercing"
  - name: "Ranged"
    desc: "⬻ hand crossbow +12 (range increment 60 feet, reload 1) __Damage__ 1d6 piercing"
  - name: "Ranged"
    desc: "⬻ alchemical grenade +13 (range increment 20 feet, [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|Splash]]) __Damage__ 2d6 acid, cold, or fire plus 2 [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent damage]] and 2 [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage of the same type"
abilities_bot:
  - name: "Cheek Pouches"
    desc: "A ratfolk grenadier has stretchy cheek pouches that can store up to 1 cubic foot of objects (though no more than 4 light items). The ratfolk can remove or store an item using the Interact action. As long as the ratfolk has at least one object in their cheek pouches, their speech is noticeably difficult to understand."
  - name: "Quick Grenadier"
    desc: "⬻ The ratfolk grenadier draws an alchemical grenade with an Interact action and throws it as a ranged Strike."
  - name: "Quick Stow"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The ratfolk grenadier stores one held item of light or negligible Bulk in their cheek pouches."
  - name: "Swarming"
    desc: "A ratfolk grenadier can end their movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
sourcebook: "_Monster Core_, page 289."
```

```encounter-table
name: Ratfolk Grenadier
creatures:
  - 1: Ratfolk Grenadier
```

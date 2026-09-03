---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Solar Crow"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/large
statblock: inline
name: "Solar Crow"
level: 10
source: "Rage of Elements"
aon_id: "creature-2634"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2634"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Solar Crow"
level: "Creature 10"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +22, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +21, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +19, Sun Lore +18, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +22"
abilityMods: [2, 6, 2, 0, 3, 5]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a solar crow's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +22; __Will__: +17"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Glow"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]]) 25 feet. The solar crow casts bright light in a 25-foot emanation (and dim light for the next 25 feet)."
  - name: "Glinting Wing"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]])"
  - name: "Trigger"
    desc: "A creature within 120 feet attempts to target the solar crow"
  - name: "Effect"
    desc: "The solar crow defensively repositions a wing to shine light into the attacker's eyes. The target is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for the duration of the triggering effect, granting the solar crow concealment against it."
speed: "20 feet, fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ beak +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d10+8 piercing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ talon +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d10+8 slashing plus 2d6 fire plus Grab"
abilities_bot:
  - name: "Blinding Heat"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The solar crow expands its wings and unleashes blazing hot, blinding light in a 120-foot emanation. Each creature in the area takes 9d6 fire damage with a DC 29 Reflex save. The crow can't use Blinding Heat again for 1d4 rounds, and its glow aura is deactivated during this time."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage and is [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] for 1 round."
  - name: "Failure"
    desc: "The creature takes full damage and is [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] for 1 round."
  - name: "Critical Failure"
    desc: "The creature takes double damage and is blinded for 1 minute."
  - name: "Burning Talons"
    desc: "A creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] by the solar crow takes 1d4 persistent fire damage. It can't recover from this damage while grabbed by the crow."
  - name: "Snatch"
    desc: "A solar crow can Fly at half Speed while it has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]] in its talons, carrying that creature along with it. Story of Infamy Ancient tales from dragon-ruled Tian Xia tell of a flock of solar crows who wreaked havoc upon the Plane of Wood, driving an herb that could grant immortality to extinction before coming to terrorize Tian Xia itself. All but one of the crows were then shot down by a legendary archer."
sourcebook: "_Rage of Elements_, page 128."
```

```encounter-table
name: Solar Crow
creatures:
  - 1: Solar Crow
```

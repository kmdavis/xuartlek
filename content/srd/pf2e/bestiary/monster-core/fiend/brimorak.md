---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Brimorak"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Brimorak"
level: 5
source: "Monster Core"
aon_id: "creature-2896"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2896"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Brimorak"
level: "Creature 5"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision, smoke vision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]]; telepathy 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +10, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +12"
abilityMods: [4, 3, 4, 1, 1, 2]
abilities_top:
  - name: "Extinguishing Aversion"
    desc: "Dousing a brimorak with water, either ordinary water or from a [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] effect, causes no physical harm to the fiend but deals 3d6 mental damage. Fully immersing the brimorak in water deals 5d6 mental damage per round."
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a brimorak's vision; they ignore the [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]] condition from smoke."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +15; __Ref__: +12; __Will__: +10"
hp: 80
health:
  - name: "HP"
    desc: "80; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ cold iron 5, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Boiling Blood"
    desc: "Each time an adjacent creature deals slashing or piercing damage to the brimorak, the attacker is sprayed with the brimorak's boiling blood, which deals 2d4 fire damage (DC 19 basic Reflex save)."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flaming sword +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+4 slashing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ hoof +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d4+4 bludgeoning plus 1d6 fire"
abilities_bot:
  - name: "Flaming Weapon"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]]) A brimorak's hooves and any weapon they wield burst into flame. They can also Interact to create a sword of fire and steel, which dissolves if it leaves their grip."
  - name: "Frothing Spew"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) The brimorak spits their boiling blood in a 20-foot line that deals 6d6 fire damage (DC 21 basic Reflex save). Creatures that fail the save also fall prone as they slip in the greasy blood. The brimorak can't use Frothing Spew again for 1d4 rounds."
  - name: "Fume"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|Fire]])"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The brimorak emits a cloud of thick black smoke in a 10-foot burst adjacent to them. The cloud remains for 1 minute. All creatures within the smoke become [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], and all creatures outside the smoke become concealed to creatures within it. A creature that enters or begins its turn within the smoke it must succeed at a DC 21 Fortitude save or become [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]] (sickened 2 on a critical failure)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/ignition|Ignition]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/fireball|Fireball]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]]"
  - name: "Rituals"
    desc: "DC 21 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 77."
```

```encounter-table
name: Brimorak
creatures:
  - 1: Brimorak
```

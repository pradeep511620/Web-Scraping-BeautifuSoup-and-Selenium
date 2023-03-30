import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re




myresult=['https://www.crescenttool.com/products/storage/chests/2-651990-30-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/2-652990-36-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/2-653990-42-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/2-654990-48-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/2-655990-60-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/2-656990-48-site-vaulttm-heavy-duty-high-capacity-chest',
'https://www.crescenttool.com/products/storage/chests/2-658990-72-site-vaulttm-heavy-duty-chest',
'https://www.crescenttool.com/products/storage/chests/cjb635990-36-tradesman-steel-chest',
'https://www.crescenttool.com/products/storage/chests/cjb636990-42-tradesman-steel-chest',
'https://www.crescenttool.com/products/storage/chests/cjb637990-48-tradesman-steel-chest',
'https://www.crescenttool.com/products/storage/chests/cjb638990-60-tradesman-steel-chest',
'https://www.crescenttool.com/products/storage/chests/2d-656990-48-site-vaulttm-heavy-duty-chests-drawer',
'https://www.crescenttool.com/products/storage/chests/2dl-656990-48-site-vaulttm-heavy-duty-chests-drawer-and-lid-storage',
'https://www.crescenttool.com/products/storage/chests/1-680990-60-slope-lid-chest',
'https://www.crescenttool.com/products/storage/chests/650990d-welders-box',
'https://www.crescenttool.com/products/storage/chests/651990d-embedded-lock-small-chest',
'https://www.crescenttool.com/products/storage/chests/659990-hasp-lock-small-chest',
'https://www.crescenttool.com/products/storage/chests/1-657990-60-high-capacity-drop-front-chest',
'https://www.crescenttool.com/products/storage/accessories-and-parts/626990-removable-tray-637990-638990',
'https://www.crescenttool.com/products/storage/accessories-and-parts/627990-28-316-steel-removable-tray-1-656990',
'https://www.crescenttool.com/products/storage/accessories-and-parts/628990-removable-tray-636990',
'https://www.crescenttool.com/products/storage/accessories-and-parts/620990-removable-tray-635990',
'https://www.crescenttool.com/products/storage/accessories-and-parts/1-321990-6-casters-set-4',
'https://www.crescenttool.com/products/storage/accessories-and-parts/1-320993-6-casters-set-4',
'https://www.crescenttool.com/products/storage/accessories-and-parts/82936-touch-paint-redrust-color-12-oz-can',
'https://www.crescenttool.com/products/storage/cabinets/1-694990-24-deep-heavy-duty-two-door-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-695990-32-deep-heavy-duty-four-door-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-697990-24-deep-heavy-duty-two-door-open-side-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-698990-30-deep-heavy-duty-two-door-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-679990-drawer-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-693990-24-deep-extra-heavy-duty-bin-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/692990-rolling-clam-shell-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/675990-rolling-work-bench-2-drawers-2-shelves-4-casters',
'https://www.crescenttool.com/products/storage/cabinets/675996-rolling-work-bench-2-drawers-2-shelves-6-casters',
'https://www.crescenttool.com/products/storage/cabinets/676990-rolling-work-bench-4-drawers-1-shelf-4-casters',
'https://www.crescenttool.com/products/storage/cabinets/676996-rolling-work-bench-4-drawers-1-shelf-6-casters',
'https://www.crescenttool.com/products/storage/cabinets/677990-rolling-work-bench-body-6-casters-add-drawers-shelves',
'https://www.crescenttool.com/products/storage/cabinets/678990-rolling-work-bench-6-drawers-1-shelf-6-casters',
'https://www.crescenttool.com/products/storage/cabinets/605990-2-12-deep-replacement-drawer-rolling-work-bench-models-675-676',
'https://www.crescenttool.com/products/storage/cabinets/606990-4-12-deep-replacement-drawer-rolling-work-bench-models-675-676',
'https://www.crescenttool.com/products/storage/cabinets/607990-5-12-deep-replacement-drawer-rolling-work-bench-models-675-676',
'https://www.crescenttool.com/products/storage/cabinets/608990-replacement-shelf-rolling-work-benches-models-677-678',
'https://www.crescenttool.com/products/storage/cabinets/609990-2-12-deep-replacement-drawer-rolling-work-bench-models-677-678',
'https://www.crescenttool.com/products/storage/cabinets/610990-4-12-deep-replacement-drawer-rolling-work-bench-models-677-678',
'https://www.crescenttool.com/products/storage/cabinets/611990-5-12-deep-replacement-drawer-rolling-work-bench-models-677-678',
'https://www.crescenttool.com/products/storage/cabinets/612990-add-push-handle-rolling-work-benches',
'https://www.crescenttool.com/products/storage/cabinets/616990-10-deep-replacement-drawer-rolling-work-bench-models-675-676',
'https://www.crescenttool.com/products/storage/cabinets/617990-10-deep-replacement-drawer-rolling-work-bench-models-677-678',
'https://www.crescenttool.com/products/storage/cabinets/1-400990-65-mesh-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-401990-49-mesh-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-402990-33-mesh-cabinet',
'https://www.crescenttool.com/products/storage/cabinets/1-403990-65-mesh-cabinet',
'https://www.crescenttool.com/products/storage/field-office/1-674990-field-office',
'https://www.crescenttool.com/products/storage/field-office/1-510990-mobile-field-office',
'https://www.crescenttool.com/products/storage/field-office/1-669990-tradesman-field-office',
'https://www.crescenttool.com/products/storage/piano-boxes/640990-60-long-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-681990-01-48-site-vaulttm-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-682990-01-60-site-vaulttm-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-683990-01-60-site-vaulttm-drop-front-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-684990-01-74-site-vaulttm-drop-front-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-685990-01-74-site-vaulttm-high-capacity-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-688990-01-60-site-vaulttm-short-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2-689990-01-74-site-vaulttm-piano-box',
'https://www.crescenttool.com/products/storage/piano-boxes/2d-681990-48-site-vaulttm-heavy-duty-piano-boxes-drawer',
'https://www.crescenttool.com/products/storage/piano-boxes/2d-682990-60-site-vaulttm-heavy-duty-piano-boxes-drawer',
'https://www.crescenttool.com/products/storage/safety/812990-2-gallon-type-i-safety-can-gasoline-flammable-liquids-red',
'https://www.crescenttool.com/products/storage/safety/812990y-2-gallon-type-i-safety-can-diesel-yellow',
'https://www.crescenttool.com/products/storage/safety/815990-5-gallon-type-i-safety-can-gasoline-flammable-liquids-red',
'https://www.crescenttool.com/products/storage/safety/815990y-5-gallon-type-i-safety-can-diesel-yellow',
'https://www.crescenttool.com/products/storage/safety/812990f-2-gallon-type-i-safety-can-gasoline-flammable-liquids-red-funnel',
'https://www.crescenttool.com/products/storage/safety/815990f-5-gallon-type-i-safety-can-gasoline-flammable-liquids-red-funnel',
'https://www.crescenttool.com/products/storage/safety/812990yf-2-gallon-type-i-safety-can-diesel-yellow-funnel',
'https://www.crescenttool.com/products/storage/safety/815990yf-5-gallon-type-i-safety-can-diesel-yellow-funnel',
'https://www.crescenttool.com/products/storage/safety/800990-replacement-funnel',
'https://www.crescenttool.com/products/storage/safety/830990-6-replacement-nozzle',
'https://www.crescenttool.com/products/storage/safety/835990-9-replacement-nozzle',
'https://www.crescenttool.com/products/storage/safety/822990-2-gallon-type-ii-safety-can-gasoline-flammable-liquids-red',
'https://www.crescenttool.com/products/storage/safety/825990-5-gallon-type-ii-safety-can-gasoline-flammable-liquids-red',
'https://www.crescenttool.com/products/storage/safety/822990y-2-gallon-type-ii-safety-can-diesel-yellow',
'https://www.crescenttool.com/products/storage/safety/825990y-5-gallon-type-ii-safety-can-diesel-yellow',
'https://www.crescenttool.com/products/storage/safety/1-750620-12-gallon-pesticide-manual-close-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-753620-30-gallon-pesticide-manual-close-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-756620-45-gallon-pesticide-manual-close-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-758620-60-gallon-pesticide-manual-close-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-759620-90-gallon-pesticide-manual-close-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-750610-12-gallon-combustible-manual-close-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-753610-30-gallon-combustible-manual-close-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-756610-45-gallon-combustible-manual-close-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-758610-60-gallon-combustible-manual-close-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-759610-90-gallon-combustible-manual-close-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-750640-12-gallon-flammable-manual-close-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-753640-30-gallon-flammable-manual-close-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-756640-45-gallon-flammable-manual-close-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-758640-60-gallon-flammable-manual-close-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-759640-90-gallon-flammable-manual-close-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-754620-30-gallon-pesticide-self-closing-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-757620-45-gallon-pesticide-self-closing-safety-cabinet-green',
'https://www.crescenttool.com/products/storage/safety/1-754610-30-gallon-combustible-self-closing-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-757610-45-gallon-combustible-self-closing-safety-cabinet-red',
'https://www.crescenttool.com/products/storage/safety/1-754640-30-gallon-flammable-self-closing-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/safety/1-757640-45-gallon-flammable-self-closing-safety-cabinet-yellow',
'https://www.crescenttool.com/products/storage/transfer-tanks/433000-74-gallon-l-shaped-tank-removable-chest-aluminum-fuel-n',
'https://www.crescenttool.com/products/storage/transfer-tanks/437000-100-gallon-l-shaped-aluminum-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/438000-100-gallon-rectangular-aluminum-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/439000-50-gallon-square-aluminum-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/498000-100-gallon-white-l-shaped-fuel-n-tooltm-ready-steel-liquid',
'https://www.crescenttool.com/products/storage/transfer-tanks/498002-100-gallon-black-l-shaped-fuel-n-tooltm-ready-steel-liquid',
'https://www.crescenttool.com/products/storage/transfer-tanks/480000-100-gallon-white-l-shaped-steel-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/480002-100-gallon-black-l-shaped-steel-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/482000-48-gallon-white-l-shaped-steel-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/484000-100-gallon-white-rectangular-steel-liquid-transfer-tank',
'https://www.crescenttool.com/products/storage/transfer-tanks/484002-100-gallon-black-rectangular-steel-liquid-transfer-tank',
'https://www.crescenttool.com/products/storage/transfer-tanks/485000-50-gallon-white-square-steel-liquid-transfer-tank-trucks',
'https://www.crescenttool.com/products/storage/transfer-tanks/486000-36-gallon-white-vertical-fuel-n-tooltm-ready-steel-liquid',
'https://www.crescenttool.com/products/storage/transfer-tanks/487000-88-gallon-white-low-profile-l-shaped-steel-liquid-transfer',
'https://www.crescenttool.com/products/storage/transfer-tanks/488000-85-gallon-white-low-profile-l-shaped-steel-liquid-transfer',
'https://www.crescenttool.com/products/storage/transfer-tanks/488002-85-gallon-black-low-profile-l-shaped-steel-liquid-transfer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/661980-storalltm-9-tall-heavy-duty-steel-drawer-storage',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/662980-storalltm-9-tall-heavy-duty-steel-drawer-storage',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/663980-storalltm-9-tall-heavy-duty-steel-drawer-storage',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/664980-storalltm-9-tall-heavy-duty-steel-drawer-storage',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/665980-storalltm-13-tall-heavy-duty-steel-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/666980-storalltm-13-tall-heavy-duty-steel-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/667980-storalltm-13-tall-heavy-duty-steel-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/668980-storalltm-13-tall-heavy-duty-steel-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1401980-1-drawer-long-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1402980-2-drawer-long-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1403980-3-drawer-long-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1404980-4-drawer-long-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1407980-2-drawer-long-stacked-heavy-duty-aluminum',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1408980-3-drawer-long-stacked-heavy-duty-aluminum',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1409980-4-drawer-long-stacked-heavy-duty-aluminum',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1405980-3-drawer-short-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1410980-plastic-drawer-divider',
'https://www.crescenttool.com/products/storage/truck-boxes/drawer-storage/1406980-6-drawer-short-floor-heavy-duty-aluminum-drawer',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/pan1441000-48-12-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/pan1441002-48-12-black-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/pan1442000-58-12-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/pan1442002-58-12-black-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/psn1451000-47-12-white-steel-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/psn1451002-47-12-black-steel-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/psn1452000-58-12-white-steel-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/psn1452002-58-12-black-steel-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/1-312000-49-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/1-312002-49-black-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/1-313000-59-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/1-313002-59-black-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/innersides/1-314000-72-aluminum-innerside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/570000-44-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/570002-44-black-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/571000d-65-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/571002d-65-black-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/572000-72-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/572002d-72-black-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/573000-88-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/573002-88-black-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/574000d-96-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/574002d-96-black-aluminum-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/575000-44-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/576000-65-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/577000-72-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/577002-72-black-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/578000-88-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/topsides/579000-96-steel-topside-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1420000-61-aluminum-fullsize-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1420002-61-black-aluminum-fullsize-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1421000-46-aluminum-compact-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1421002-46-black-aluminum-compact-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1424000-61-aluminum-extra-wide-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/pah1424002-61-black-aluminum-extra-wide-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/1-350000-60-gear-locktm-aluminum-fullsize-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/1-350002-60-gear-locktm-black-aluminum-fullsize-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/220000d-37-portable-aluminum-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/221000d-49-portable-aluminum-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/222000d-57-portable-aluminum-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/808000-36-aluminum-portable-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/896260-58-aluminum-fullsize-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/896262-58-black-aluminum-fullsize-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/899260-46-aluminum-compact-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/405000d-33-aluminum-trailer-tongue-box',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/405002-33-black-aluminum-trailer-tongue-box',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/410000d-48-aluminum-extra-wide-trailer-tongue-box',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/810000-32-steel-portable-truck-chest-mounting-base-plates',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/814000-32-steel-mid-size-hopper-chest-34-cubic-ft',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/815000-48-steel-large-capacity-hopper-chest-115-cubic-ft',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/817980-white-steel-heavy-duty-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/818980-white-steel-compact-heavy-duty-truck-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/truck-chests/dyh1453002-hybrid-fullsize-portable-chest',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/228000-18-x-18-underbed-mounting-brackets',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/229000-24-x-24-underbed-mounting-brackets',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/790980-white-steel-underbed-box-24-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/790982-black-steel-underbed-box-24-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/791980-white-steel-underbed-box-30-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/791982-black-steel-underbed-box-30-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/792980-white-steel-underbed-box-36-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/792982-black-steel-underbed-box-36-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/793980-white-steel-underbed-box-48-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/793982-black-steel-underbed-box-48-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/794980-white-steel-underbed-box-60-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/794982-black-steel-underbed-box-60-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7924160-white-steel-underbed-box-24-x-16-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7924162-black-steel-underbed-box-24-x-16-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7930240-white-steel-underbed-box-30-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7930242-black-steel-underbed-box-30-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936140-white-steel-underbed-box-36-x-12-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936142-black-steel-underbed-box-36-x-12-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936160-white-steel-underbed-box-36-x-16-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936162-black-steel-underbed-box-36-x-16-x-14',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936240-white-steel-underbed-box-36-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7936242-black-steel-underbed-box-36-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7924240-white-steel-underbed-box-24-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7924242-black-steel-underbed-box-24-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7948240-white-steel-underbed-box-48-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7948242-black-steel-underbed-box-48x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7960240-white-steel-underbed-box-48-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7960242-black-steel-underbed-box-60-x-24-x-24',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7972180-white-steel-underbed-box-72-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/underbodies/7972182-black-steel-underbed-box-72-x-18-x-18',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1455000-steel-single-lid-fullsize-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1455002-black-steel-single-lid-fullsize-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1456000-steel-single-lid-fullsize-deep-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1456002-black-steel-single-lid-fullsize-deep-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1457000-white-steel-single-lid-fullsize-deep-extra-wide',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1457002-black-steel-single-lid-fullsize-deep-extra-wide',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1458000-steel-single-lid-compact-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1458002-black-steel-single-lid-compact-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1460000-steel-gull-wing-fullsize-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1460002-black-steel-gull-wing-fullsize-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1461000-white-steel-gull-wing-fullsize-deep-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/psc1461002-black-steel-gull-wing-fullsize-deep-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1701000-limited-edition-aluminum-single-lid-deep-super-duty',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1357000-low-profile-aluminum-single-lid-fullsize',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1357002-low-profile-black-aluminum-fullsize-single-lid',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1580000-aluminum-single-lid-fullsize-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1580002-black-aluminum-single-lid-fullsize-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1582000-aluminum-single-lid-fullsize-deep-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1582002-black-aluminum-single-lid-fullsize-deep',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1584000-aluminum-single-lid-super-duty-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1584002-black-aluminum-single-lid-super-duty-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1585000-aluminum-single-lid-fullsize-super-deep',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1585002-black-aluminum-single-lid-fullsize-super-deep',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1587000-aluminum-single-lid-compact-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1587002-black-aluminum-single-lid-compact-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1589000-aluminum-single-lid-mid-size-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1589002-black-aluminum-single-lid-mid-size-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1596000-aluminum-mid-lid-aluminum-fullsize-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1597000-aluminum-mid-lid-compact-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1598000-aluminum-mid-lid-rear-hinged-fullsize-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/pac1596002-black-aluminum-mid-lid-aluminum-fullsize',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-232000-gear-locktm-aluminum-single-lid-fullsize-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-232002-gear-locktm-black-aluminum-single-lid-fullsize',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-235000-gear-locktm-aluminum-single-lid-compact-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-238000-gear-locktm-aluminum-mid-lid-fullsize-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-238002-gear-locktm-black-aluminum-mid-lid-fullsize',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-351000-gear-locktm-aluminum-low-profile-single-lid',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-351002-gear-locktm-black-aluminum-low-profile-single-lid',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-302000-aluminum-single-lid-fullsize-low-profile-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-302002-black-aluminum-fullsize-low-profile-single-lid',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-309000-aluminum-single-lid-super-duty-low-profile',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-309002-black-aluminum-single-lid-super-duty-low-profile',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-310000-aluminum-single-lid-mid-size-low-profile-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-310002-black-aluminum-mid-size-low-profile-single-lid',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-300000-aluminum-single-lid-fullsize-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-300002-black-aluminum-single-lid-fullsize-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-301000-aluminum-single-lid-fullsize-deep-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-301002-black-aluminum-single-lid-fullsize-deep-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-304000-aluminum-single-lid-mid-size-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-304002-black-aluminum-single-lid-mid-size-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-311000-aluminum-single-lid-fullsize-slimline-crossover',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-311002-black-aluminum-single-lid-fullsize-slimline',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-306000-aluminum-dual-lid-fullsize-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-306002-black-aluminum-dual-lid-fullsize-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-307000-aluminum-dual-lid-mid-size-crossover-truck-box',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/1-307002-black-aluminum-dual-lid-mid-size-crossover-truck',
'https://www.crescenttool.com/products/storage/truck-boxes/crossovers/dhc1450000-hybrid-single-lid-fullsize-crossover-truck-box']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+result.status_code)

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    title = soup.find("div",class_="field field--name-field-long-description field--type-string field--label-hidden field__item")
    a = (title.text.strip() if title else "not given")
    print(a)

    price = soup.find("span",class_="field field--name-title field--type-string field--label-hidden")
    pr = (price.text.strip() if price else "not given")
    print(pr)


    c = (product_url)
    print(c)
    list1 = []

    feat=soup.find_all("li",class_="field__item")
    l=[None]*25
    hii=0
    for f in feat:
        l[hii]=f.text
        hii=hii+1
    print(l)
    specs = soup.find("div", class_="field field--name-field-product-specifications field--type-entity-reference field--label-hidden field__items").find_all("div",class_="field__item")
    ll=[None]*25
    hi=0
    for spec in specs:
         ll[hi]=spec.text
         hi=hi+1



    for z in range(0,25):
     save_details: TextIO = open("Jobox_final_data.txt", "a+", encoding="utf-8")
     save_details.write("\n"+pr+"\t"+c+"\t"+a+"\t"+str(l[z])+"\t"+str(ll[z]))
     save_details.close()
     print("\n**Record stored into txt file.**")

 except AttributeError:

   pass

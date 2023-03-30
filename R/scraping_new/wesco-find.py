import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re


myresult=['https://catalog.wescomfg.com/viewitems/drum-handling-equipment/attachment-ergonomic-drum-handlers-fork-drum-grabs',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-trucks-steel-aluminum-pail-truck-pail-tipper',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/knock-down--kd--drum-trucks',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-trucks-carriers-dispensers',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/fork-truck-drum-dispensers-poly-drum-lifters',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-lifters-universal-drum-lifter',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-dollies-steel-aluminum-stainless-steel',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/stainless-steel-drum-dollies',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-slings-and-dispensers',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-racks-cradles',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/fm-approved-drum-faucets-valves-vents-gauges-wires',
'https://catalog.wescomfg.com/viewitems/drum-handling-equipment/drum-wrenches-deheaders-pumps-drip-pans',
'https://catalog.wescomfg.com/viewitems/hand-trucks/100-series-industrial-duty-steel-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/convertible-steel-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/greenline-standard-duty-steel-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/touch-n-tilt-drum-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/heavy-duty-steel-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/economy-tilting-high-frame-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/aluminum-cobra-lite-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/aluminum-cobra-convertible-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/position-cobra-spartan-iii-powered-cobrapro-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/liftkar-hd-stairking-and-stair-climbing-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/power-liftkar-hd-stairclimbing-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/liftkar-sal-power-stairclimbing-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/wesco-steel-vending-appliance-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/cylinder-lifts-carts-and-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/drum-hand-trucks',
'https://catalog.wescomfg.com/viewitems/hand-trucks/wesco-wheels',
'https://catalog.wescomfg.com/viewitems/advantage-pallet-trucks/advantage-manual-pallet-trucks',
'https://catalog.wescomfg.com/viewitems/advantage-pallet-trucks/advantage-power-pallet-trucks',
'https://catalog.wescomfg.com/viewitems/lift-equipment/s-manual-powered-pallet-jack-chock-backrest-guards',
'https://catalog.wescomfg.com/viewitems/lift-equipment/steel-pedalifts-winch-hydraulic',
'https://catalog.wescomfg.com/viewitems/lift-equipment/triple-truck-aluminum-pedalifts',
'https://catalog.wescomfg.com/viewitems/lift-equipment/hand-winch-lifts',
'https://catalog.wescomfg.com/viewitems/lift-equipment/kers-thrifty-stackers-drum-1-000-lb-winch-stackers',
'https://catalog.wescomfg.com/viewitems/lift-equipment/fork-stackers',
'https://catalog.wescomfg.com/viewitems/lift-equipment/ectric-value-lifts-office-lifts-mini-winch-stacker',
'https://catalog.wescomfg.com/viewitems/lift-equipment/counter-balance-stackers-fork-models',
'https://catalog.wescomfg.com/viewitems/lift-equipment/powered-stackers-platform-fixed-adjustable',
'https://catalog.wescomfg.com/viewitems/lift-equipment/-from-200-to-6000-lb-manual-and-powered-lift',
'https://catalog.wescomfg.com/viewitems/lift-equipment/wesco-hclt-series-precision-lift-tables',
'https://catalog.wescomfg.com/viewitems/lift-equipment/scissors-lift-tables-die-lift-table',
'https://catalog.wescomfg.com/viewitems/lift-equipment/chain-hoist-trolleys',
'https://catalog.wescomfg.com/viewitems/lift-equipment/pallet-leveler',
'https://catalog.wescomfg.com/viewitems/lift-equipment/rais-n-rol-machinery-movers',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco--foot-operated-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco-foot-operated-electric-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco-foot-powered-portable-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco-long-deck-hydraulic-foot-operated-lift-table',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco-manual-push-pull-die-handling-conveyor',
'https://catalog.wescomfg.com/viewitems/lexco-hydraulic-lift-tables-die-handlers/lexco--die-handler',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/power-drive-platform-trucks',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/wire-cage-package-platform-panel-carts',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/aluminum-steel-wood-u-boats',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/ng-handle-platform-trucks-steel-stainless-aluminum',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/plastic-steel-service-carts',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/ble-top-office-carts-file-cabinet-truck-desk-mover',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/plastic-platform-lightweight-folding-trucks',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/heavy-duty-machine-dolly-rollers',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/plastic-box-trucks',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/casters',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/bumpers-1',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/handles',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/wood-dollies',
'https://catalog.wescomfg.com/viewitems/platform-trucks-carts-dollies/tilt-carts',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/dock-lights-strapping-truck-and-tools',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/railer-stabilizing-jacks-cargo-bars-pallet-pullers',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/transfer-cart-fork-extensions-maintenance-platform',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/nsf-approved-wire-shelving-accessories',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/wesco-wheels',
'https://catalog.wescomfg.com/viewitems/ck-and-shipping-equipment-wire-shelving-and-wheels/dock-seals',
'https://catalog.wescomfg.com/viewitems/lift-tables/-from-200-to-6000-lb-manual-and-powered-lift',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco--foot-operated-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco-foot-operated-electric-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco-foot-powered-portable-hydraulic-lift-table',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco-long-deck-hydraulic-foot-operated-lift-table',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco-manual-push-pull-die-handling-conveyor',
'https://catalog.wescomfg.com/viewitems/lift-tables/lexco--die-handler',
'https://catalog.wescomfg.com/viewitems/all-categories/stainless-steel-products']

for row in myresult:

 try:

    product_url = row

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+str(result.status_code))

    #a = (result.content.decode())


    soup = BeautifulSoup(result.content,'html.parser')




    bread = soup.find_all("a",class_="plp-itemlink")
    list1 = []
    for b in bread:
        list1.append(b.get("href"))
    print(list1)
    for i in range(0,len(list1)):
     save_details: TextIO = open("wesco---find.txt", "a+", encoding="utf-8")
     save_details.write("\n"+list1[i])
     save_details.close()
     print("\n**Record stored into txt file.**")






 except AttributeError:

   pass

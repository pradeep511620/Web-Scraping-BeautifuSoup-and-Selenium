import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re




myresult=['https://www.ams-samplers.com/2-serrated-split-core-tip/',
'https://www.ams-samplers.com/2-x-12-slotted-core-sampler-cup/',
'https://www.ams-samplers.com/2-stainless-split-core-cap-1-1-4-direct-push-thread/',
'https://www.ams-samplers.com/2-soil-core-sampler-cap-1-1-4-direct-push-thread/',
'https://www.ams-samplers.com/2-drive-extension-1-1-4-direct-push-thread/',
'https://www.ams-samplers.com/gas-powered-hammer-head-w-20-removable-cross-handle-1-1-4-direct-push-thread/',
'https://www.ams-samplers.com/2-x-12-scs-cup/',
'https://www.ams-samplers.com/2-split-scs-core-tip/',
'https://www.ams-samplers.com/2-x-12-split-scs-cup-set/',
'https://www.ams-samplers.com/gas-powered-redi-boss-hammer-with-3-1-8-barrel/',
'https://www.ams-samplers.com/core-n-one-soil-handle/',
'https://www.ams-samplers.com/core-n-load-soil-syringe-case-of-20/',
'https://www.ams-samplers.com/lock-n-load-soil-syringe-case-of-50/',
'https://www.ams-samplers.com/multi-stage-soil-core-sampler-complete-hex-quick-pin/',
'https://www.ams-samplers.com/2-plastic-end-cap/',
'https://www.ams-samplers.com/universal-slip-wrench/',
'https://www.ams-samplers.com/2-x-12-sst-liner/',
'https://www.ams-samplers.com/2-ms-scs-solid-cap-w-3-4-threads/',
'https://www.ams-samplers.com/serrated-ms-scs-core-tip/',
'https://www.ams-samplers.com/2-multi-stage-scs-complete/',
'https://www.ams-samplers.com/2-ms-scs-auger-tip/',
'https://www.ams-samplers.com/2-ms-scs-core-tip/',
'https://www.ams-samplers.com/2-x-12-ms-sludge-scs-base/',
'https://www.ams-samplers.com/2-x-12-ms-section/',
'https://www.ams-samplers.com/ms-scs-solid-cap/',
'https://www.ams-samplers.com/3-1-4-stainless-steel-soil-core-sampling-mini-kit-hex-quick-pin/',
'https://www.ams-samplers.com/3-plastic-end-cap/',
'https://www.ams-samplers.com/2-plastic-end-cap/',
'https://www.ams-samplers.com/universal-slip-wrench/',
'https://www.ams-samplers.com/1-1-2-plastic-end-cap/',
'https://www.ams-samplers.com/2-scs-cap-w-3-4-threads/',
'https://www.ams-samplers.com/2-sst-scs-cap/',
'https://www.ams-samplers.com/2-1-2-sst-scs-cap-w-3-4-threads/',
'https://www.ams-samplers.com/2-scs-cap-w-5-8-threaded-connection/',
'https://www.ams-samplers.com/1-1-2-x-12-sst-scs-cup/',
'https://www.ams-samplers.com/1-1-2-x-12-sst-scs-cup-cap/',
'https://www.ams-samplers.com/1-1-2-x-12-sst-scs-complete/',
'https://www.ams-samplers.com/2-1-2-sst-scs-cap/',
'https://www.ams-samplers.com/2-1-2-plastic-end-caps/',
'https://www.ams-samplers.com/2-x-12-sst-scs-cup/',
'https://www.ams-samplers.com/3-x-6-sst-scs-cup/',
'https://www.ams-samplers.com/2-1-2-x-6-sst-scs-cup/',
'https://www.ams-samplers.com/1-1-2-x-6-sst-scs-cup/',
'https://www.ams-samplers.com/2-x-4-sst-scs-cup/',
'https://www.ams-samplers.com/2-x-6-sst-scs-cup/',
'https://www.ams-samplers.com/2-x-3-sst-scs-cup/',
'https://www.ams-samplers.com/2-x-2-sst-scs-cup/',
'https://www.ams-samplers.com/2-sst-scs-cap-w-3-4-threads/',
'https://www.ams-samplers.com/2-x-12-sst-scs-cup-cap/',
'https://www.ams-samplers.com/3-x-6-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-1-2-x-6-sst-scs-cup-cap/',
'https://www.ams-samplers.com/1-1-2-x-6-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-6-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-4-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-3-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-2-sst-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-12-sst-scs-complete/',
'https://www.ams-samplers.com/3-1-4-x-10-stainless-steel-soil-recovery-auger-complete-hex-quick-pin/',
'https://www.ams-samplers.com/3-1-4-x-10-soil-recovery-auger-complete-hex-quick-pin/',
'https://www.ams-samplers.com/3-plastic-end-cap/',
'https://www.ams-samplers.com/2-plastic-end-cap/',
'https://www.ams-samplers.com/3-1-4-x-10-sra-complete/',
'https://www.ams-samplers.com/3-1-4-x-12-sra-complete/',
'https://www.ams-samplers.com/3-1-4-x-10-sst-sra-complete/',
'https://www.ams-samplers.com/3-1-4-x-12-sst-sra-complete/',
'https://www.ams-samplers.com/2-1-4-x-8-sra-complete/',
'https://www.ams-samplers.com/2-1-4-x-10-sra-complete/',
'https://www.ams-samplers.com/2-1-4-x-8-sst-sra-complete/',
'https://www.ams-samplers.com/2-1-4-x-10-sst-sra-complete/',
'https://www.ams-samplers.com/2-1-4-x-8-sra-cylinder-body/',
'https://www.ams-samplers.com/2-1-4-x-10-sra-cylinder-only/',
'https://www.ams-samplers.com/2-1-4-sra-solid-cap/',
'https://www.ams-samplers.com/2-1-4-sra-hollow-cap/',
'https://www.ams-samplers.com/3-1-4-x-10-sra-cylinder-body/',
'https://www.ams-samplers.com/3-1-4-x-12-sra-cylinder-body/',
'https://www.ams-samplers.com/3-1-4-sra-solid-cap/',
'https://www.ams-samplers.com/3-1-4-sra-hollow-cap/',
'https://www.ams-samplers.com/2-1-4-x-8-sst-sra-cylinder-body/',
'https://www.ams-samplers.com/2-1-4-x-10-sst-sra-cylinder-body/',
'https://www.ams-samplers.com/3-1-4-x-10-sst-sra-cylinder-body/',
'https://www.ams-samplers.com/3-1-4-x-12-sst-sra-cylinder-body/',
'https://www.ams-samplers.com/universal-slip-wrench/',
'https://www.ams-samplers.com/3-x-10-plastic-liner/',
'https://www.ams-samplers.com/3-x-12-plastic-liner/',
'https://www.ams-samplers.com/2-x-8-plastic-liner/',
'https://www.ams-samplers.com/2-x-10-plastic-liner/',
'https://www.ams-samplers.com/2-1-2-x-12-split-soil-core-sampler-w-both-tips-hex-quick-pin/',
'https://www.ams-samplers.com/2-x-12-split-soil-core-sampler-w-both-tips-signature/',
'https://www.ams-samplers.com/2-split-core-sampler-cap/',
'https://www.ams-samplers.com/1-3-8-split-core-sampler-cap/',
'https://www.ams-samplers.com/1-3-8-x-6-split-core-sampler-with-core-tip/',
'https://www.ams-samplers.com/2-x-6-split-core-sampler-w-core-tip-3-4-threaded/',
'https://www.ams-samplers.com/3-1-4-x-3-signature-series-split-core-sampling-kit/',
'https://www.ams-samplers.com/1-3-8-split-scs-valved-auger-tip/',
'https://www.ams-samplers.com/1-3-8-split-scs-valved-core-tip/',
'https://www.ams-samplers.com/2-1-2-split-scs-valved-auger-tip/',
'https://www.ams-samplers.com/2-split-scs-valved-auger-tip/',
'https://www.ams-samplers.com/2-1-2-split-scs-valved-core-tip/',
'https://www.ams-samplers.com/2-split-scs-valved-core-tip/',
'https://www.ams-samplers.com/2-split-scs-cylinder-coupling/',
'https://www.ams-samplers.com/2-1-2-split-scs-cylinder-coupling/',
'https://www.ams-samplers.com/2-1-2-split-scs-auger-tip/',
'https://www.ams-samplers.com/2-split-scs-auger-tip/',
'https://www.ams-samplers.com/2-1-2-x-12-split-scs-w-both-tips/',
'https://www.ams-samplers.com/2-1-2-x-6-split-scs-w-both-tips/',
'https://www.ams-samplers.com/2-x-12-split-scs-w-both-tips/',
'https://www.ams-samplers.com/2-x-6-split-scs-w-both-tips/',
'https://www.ams-samplers.com/1-3-8-split-scs-coupling/',
'https://www.ams-samplers.com/1-3-8-split-scs-core-tip/',
'https://www.ams-samplers.com/1-3-8-split-scs-auger-tip/',
'https://www.ams-samplers.com/1-3-8-split-scs-solid-cap/',
'https://www.ams-samplers.com/1-3-8-x-12-split-scs-cup-set/',
'https://www.ams-samplers.com/1-3-8-x-6-split-scs-cup-set/',
'https://www.ams-samplers.com/1-3-8-x-12-split-scs-w-both-tips/',
'https://www.ams-samplers.com/1-3-8-x-6-split-scs-w-both-tips/',
'https://www.ams-samplers.com/1-3-8-x-12-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/1-3-8-x-6-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/1-3-8-x-12-split-scs-w-core-tip/',
'https://www.ams-samplers.com/concrete-test-hammer-type-n-1/',
'https://www.ams-samplers.com/24-dual-mass-dcp-extension/',
'https://www.ams-samplers.com/12-dual-mass-dcp-drive-rod/',
'https://www.ams-samplers.com/dual-mass-disposable-tip-pack-of-100/',
'https://www.ams-samplers.com/dual-mass-disposable-tip-pack-of-25/',
'https://www.ams-samplers.com/ams-dual-mass-dcp-with-vertek-smart-dcp-complete/',
'https://www.ams-samplers.com/ams-dual-mass-dynamic-cone-penetrometer/',
'https://www.ams-samplers.com/vertek-smart-dcp/',
'https://www.ams-samplers.com/dynamic-cone-penetrometer-complete/',
'https://www.ams-samplers.com/5-external-dcp-extension-rod/',
'https://www.ams-samplers.com/2-1-2-external-dcp-extension-rod/',
'https://www.ams-samplers.com/1-dcp-drill-rod-point-holder/',
'https://www.ams-samplers.com/dcp-drive-hammer-assembly/',
'https://www.ams-samplers.com/dcp-replacement-point-with-roll-pin/',
'https://www.ams-samplers.com/1-4-x-1-1-4-dcp-spiral-pin-for-point/',
'https://www.ams-samplers.com/1-dcp-adapter-drive-w-heat-treated-drive/',
'https://www.ams-samplers.com/eijkelkamp-soil-moisture-sensor-thetaprobe-1/',
'https://www.ams-samplers.com/field-van-shear-tester-complete/',
'https://www.ams-samplers.com/16-x-32-mm-fvs-vane-0-200-kpa/',
'https://www.ams-samplers.com/20-x-40-mm-fvs-vane-0-100-kpa/',
'https://www.ams-samplers.com/geo-tester-penetrometer-1/',
'https://www.ams-samplers.com/infiltration-rings-6-id-12-od/',
'https://www.ams-samplers.com/infiltration-rings-12-id-24-od/',
'https://www.ams-samplers.com/pocket-penetrometer-1/',
'https://www.ams-samplers.com/pocket-penetrometer-adapter-foot/',
'https://www.ams-samplers.com/shaw-portablecore-drill-backpack-drill-rock-coring-kit-41mm/',
'https://www.ams-samplers.com/24-scp-starter-rod-assembly/',
'https://www.ams-samplers.com/24-scp-extension-rod-assembly/',
'https://www.ams-samplers.com/24-scp-extension-inner-rod/',
'https://www.ams-samplers.com/24-scp-starter-inner-rod/',
'https://www.ams-samplers.com/24-scp-outer-rod/',
'https://www.ams-samplers.com/standard-60-degree-scp-cone-assembly/',
'https://www.ams-samplers.com/o-ring-packing-kit-2-each/',
'https://www.ams-samplers.com/large-60-degree-scp-cone-assembly/',
'https://www.ams-samplers.com/static-cone-penetrometer-complete/',
'https://www.ams-samplers.com/sentricon-flighted-auger-kit/',
'https://www.ams-samplers.com/sentricon-auger-kit/',
'https://www.ams-samplers.com/sentricon-deluxe-kit/',
'https://www.ams-samplers.com/5-8threaded-male-to-1-2-gas-drill-adapter/',
'https://www.ams-samplers.com/5-8-compact-slide-hammer/',
'https://www.ams-samplers.com/echo-drill-edr-260-reversible/',
'https://www.ams-samplers.com/echo-drill-ea-410/',
'https://www.ams-samplers.com/echo-gas-drill-side-handle-replacement/',
'https://www.ams-samplers.com/3-core-bit-complete-w-splined-adapter/',
'https://www.ams-samplers.com/3-core-bit-complete-w-sds-max-adapter/',
'https://www.ams-samplers.com/heavy-duty-splined-adapter/',
'https://www.ams-samplers.com/heavy-duty-sds-max-adapter/',
'https://www.ams-samplers.com/7-16-heavy-duty-starter-bit/',
'https://www.ams-samplers.com/5-8-x-2-extension/',
'https://www.ams-samplers.com/port-cover-aluminum/',
'https://www.ams-samplers.com/port-cover-brass/',
'https://www.ams-samplers.com/port-cover-black/',
'https://www.ams-samplers.com/port-cover-screwdriver/',
'https://www.ams-samplers.com/3-heavy-duty-core-bit/',
'https://www.ams-samplers.com/1-1-2-x-12-clean-out-auger/',
'https://www.ams-samplers.com/1-1-2-x-12-t-bar-cleanout-auger/',
'https://www.ams-samplers.com/2-1-2-t-bar-cleanout-auger/',
'https://www.ams-samplers.com/2-1-2-clean-out-auger/',
'https://www.ams-samplers.com/2-3-4-x-24-clean-out-auger/',
'https://www.ams-samplers.com/5-8-x-4-extension/',
'https://www.ams-samplers.com/5-8-x-3-extension/',
'https://www.ams-samplers.com/18-ratcheting-cross-handle-5-8-threaded/',
'https://www.ams-samplers.com/18-rubber-coated-cross-handle-5-8-threaded/',
'https://www.ams-samplers.com/5-8threaded-male-to-splined-drill-adapter/',
'https://www.ams-samplers.com/ex-2000-top-cap-pliers/',
'https://www.ams-samplers.com/dewalt-d25773k-2-sds-max-combination-hammer-drill/',
'https://www.ams-samplers.com/36-two-piece-tile-probe/',
'https://www.ams-samplers.com/cobra-pro-gas-breaker-1-1-4-x-6-shank/',
'https://www.ams-samplers.com/hammer-anvil-cobra-pro-1-1-4-x-6/',
'https://www.ams-samplers.com/dewalt-cordless-rotary-hammer/',
'https://www.ams-samplers.com/2-one-piece-combination-edelman-auger-2ft/',
'https://www.ams-samplers.com/2-carbide-tip-1/',
'https://www.ams-samplers.com/2-hard-surfaced-tip/',
'https://www.ams-samplers.com/1-3-4-regular-auger/',
'https://www.ams-samplers.com/1-3-4-mud-auger/',
'https://www.ams-samplers.com/stc-cup-cutter/',
'https://www.ams-samplers.com/sentricon-flighted-auger-kit/',
'https://www.ams-samplers.com/sentricon-auger-kit/',
'https://www.ams-samplers.com/sentricon-deluxe-kit/',
'https://www.ams-samplers.com/flighted-auger-w-tip-adapter-1-7-8/',
'https://www.ams-samplers.com/1-7-8-tip-only-flighted-aug/',
'https://www.ams-samplers.com/one-piece-2-edelman-combination/',
'https://www.ams-samplers.com/1-7-8-flighted-auger-w-carbide-tip-and-adapter/',
'https://www.ams-samplers.com/flighted-auger-w-carbide-tip/',
'https://www.ams-samplers.com/2-dutch-auger/',
'https://www.ams-samplers.com/trelona-auger/',
'https://www.ams-samplers.com/2-1-4-regular-auger/',
'https://www.ams-samplers.com/2-1-4-mud-auger-w-2-3-4-bits/',
'https://www.ams-samplers.com/2-5-8-carbide-tip/',
'https://www.ams-samplers.com/2-5-8-hard-surfaced-tip/',
'https://www.ams-samplers.com/flighted-auger-2-1-2-w-tip-1-2-adapter/',
'https://www.ams-samplers.com/flighted-auger-only-2-1-2/',
'https://www.ams-samplers.com/flighted-auger-2-1-2-w-tip/',
'https://www.ams-samplers.com/one-piece-2-1-2-open-faced-auger/',
'https://www.ams-samplers.com/2-1-2-open-faced-auger/',
'https://www.ams-samplers.com/idaho-spoon/',
'https://www.ams-samplers.com/flighted-auger-2-1-2-w-carbide-tip-and-adapter/',
'https://www.ams-samplers.com/one-piece-2-3-4-mud-auger/',
'https://www.ams-samplers.com/one-piece-2-3-4-regular-auger/',
'https://www.ams-samplers.com/1-1-2-fluoropolymer-bottom-fill-bailer-fitting/',
'https://www.ams-samplers.com/3-4-fluoropolymer-bottom-fill-bailer-fitting/',
'https://www.ams-samplers.com/1-2-x-1-clear-polyethylene-bailer-case-of-24/',
'https://www.ams-samplers.com/7-8-fluoropolymer-bottom-fill-bailer-fitting/',
'https://www.ams-samplers.com/1-fluoropolymer-bottom-fill-bailer-fitting/',
'https://www.ams-samplers.com/7-8-stainless-steel-bailer-check-ball/',
'https://www.ams-samplers.com/3-8-stainless-steel-bailer-check-ball/',
'https://www.ams-samplers.com/1-3-4-x-3-tapered-sst-bailer/',
'https://www.ams-samplers.com/1-x-3-tapered-stainless-steel-bailer/',
'https://www.ams-samplers.com/7-8-x-3-bottom-fill-stainless-steel-bailer/',
'https://www.ams-samplers.com/3-4-x-3-bottom-fill-stainless-steel-bailer/',
'https://www.ams-samplers.com/3-8-x-18-top-fill-stainless-steel-bailer/',
'https://www.ams-samplers.com/46-x-3-clear-pvc-bailer-case-of-24/',
'https://www.ams-samplers.com/7-x-1-clear-pvc-bailer-case-of-24/',
'https://www.ams-samplers.com/7-x-3-clear-pvc-bailer-case-of-24/',
'https://www.ams-samplers.com/1-1-2-x-1-clear-pvc-bailer-case-of-24/',
'https://www.ams-samplers.com/1-1-2-x-3-clear-pvc-bailer-case-of-24/',
'https://www.ams-samplers.com/1-1-2-x-3-clear-poly-bailer-case-of-24/',
'https://www.ams-samplers.com/1-1-2-x-1-weighted-poly-bailer-case-of-24/',
'https://www.ams-samplers.com/1-1-2-x-3-weighted-poly-bailer-case-of-24/',
'https://www.ams-samplers.com/18-x-275-twisted-nylon-twine/',
'https://www.ams-samplers.com/1-1-2-x-3-stainless-steel-bailer/',
'https://www.ams-samplers.com/check-ball-stainless-steel-1-2/',
'https://www.ams-samplers.com/ptfe-bailer-fitting/',
'https://www.ams-samplers.com/1-3-4-x-3-stainless-steel-top-fill-bailer/',
'https://www.ams-samplers.com/1-1-2in-x-1ft-weighted-clear-pvc-bio-bailer-case-of-48/',
'https://www.ams-samplers.com/1-1-2in-x-3-ft-weighted-clear-pvc-bio-bailer-case-of-24/',
'https://www.ams-samplers.com/bailer-fitting-fep-5-8/',
'https://www.ams-samplers.com/1-3-4-sst-bailer-plug-only-for-top-fill-bailer/',
'https://www.ams-samplers.com/1-3-4-x-3-sst-double-check-ball-bailer/',
'https://www.ams-samplers.com/5-8-x-3-bottom-fill-stainless-steel-bailer/',
'https://www.ams-samplers.com/interface-meter-with-5-8in-probe-and-100ft-tape/',
'https://www.ams-samplers.com/interface-meter-with-5-8in-probe-and-30m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-100ft-tape/',
'https://www.ams-samplers.com/padded-carrying-case-for-water-level-and-interface-meters/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-200ft-tape/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-300ft-tape/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-30m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-60m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-5-8in-probe-and-100m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-100ft-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-200ft-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-300ft-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-30m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-60m-tape/',
'https://www.ams-samplers.com/water-level-meter-with-3-8in-probe-and-100m-tape/',
'https://www.ams-samplers.com/50-stainless-steel-mesh-screen/',
'https://www.ams-samplers.com/1-1-4-expendable-tip/',
'https://www.ams-samplers.com/twist-to-lock-connector-3-16-id/',
'https://www.ams-samplers.com/crescent-wrench-12/',
'https://www.ams-samplers.com/4ft-ams-deluxe-carrying-case-1750/',
'https://www.ams-samplers.com/1-x-24-nylon-brush/',
'https://www.ams-samplers.com/1-3-4-regular-auger/',
'https://www.ams-samplers.com/big-foot-removal-jack/',
'https://www.ams-samplers.com/5-8-x-3-extension/',
'https://www.ams-samplers.com/18-rubber-coated-cross-handle-5-8-threaded/',
'https://www.ams-samplers.com/piezometer-groundwater-sampling-kit-1/',
'https://www.ams-samplers.com/1-1-4-x-14-stainless-steel-piezometer/',
'https://www.ams-samplers.com/1-1-4-x-3-stainless-steel-extension/',
'https://www.ams-samplers.com/male-to-male-piezometer-extension-coupler/',
'https://www.ams-samplers.com/threadless-drive-adapter/',
'https://www.ams-samplers.com/piezometer-t-jack-adapter/',
'https://www.ams-samplers.com/piezometer-point-holder/',
'https://www.ams-samplers.com/piezometer-slotted-pull-adapter/',
'https://www.ams-samplers.com/3-4-heavy-duty-slide-hammer/',
'https://www.ams-samplers.com/peristaltic-pump-geopump2-ac-dc-carrying-case-battery/',
'https://www.ams-samplers.com/3-16-id-x-1-4-od-x-50-fluoropolymer-tubing/',
'https://www.ams-samplers.com/sds-max-drill-adapter-to-3-4-od/',
'https://www.ams-samplers.com/gvp-screen-50-mesh/',
'https://www.ams-samplers.com/gas-vapor-tip-umbrella/',
'https://www.ams-samplers.com/3-5-od-x-5-length-steel-bollard-in-safety-yellow/',
'https://www.ams-samplers.com/4-5-od-x-6-length-steel-bollard-in-safety-yellow/',
'https://www.ams-samplers.com/monitoring-well-manhole-8-x-12-steel-skirt-3-bolt/',
'https://www.ams-samplers.com/4-x-5-tall-square-well-protector/',
'https://www.ams-samplers.com/4-x-5-tall-square-well-protector-black-steel/',
'https://www.ams-samplers.com/6-x-5-tall-round-well-protector-black-steel/',
'https://www.ams-samplers.com/6-x-5-tall-square-well-protector-in-safety-yellow/',
'https://www.ams-samplers.com/8-x-8-steel-skirt-3-bolt-manhole/',
'https://www.ams-samplers.com/5-x-7-steel-skirt-2-bolt-manhole/',
'https://www.ams-samplers.com/4-od-5-round-well-protector-black-steel/',
'https://www.ams-samplers.com/gas-powered-redi-boss-hammer-with-3-1-8-barrel/',
'https://www.ams-samplers.com/5-8threaded-male-to-sds-plus-drill-adapter/',
'https://www.ams-samplers.com/2-hawera-carbide-bit-sds-max/',
'https://www.ams-samplers.com/hawera-2-x-17-x-22-splined-carbide-bit/',
'https://www.ams-samplers.com/2-1-2-wild-bore-sds-max/',
'https://www.ams-samplers.com/1-1-2-concrete-bit-sds-max/',
'https://www.ams-samplers.com/5-8threaded-male-to-sds-max-drill-adapter/',
'https://www.ams-samplers.com/5-8threaded-male-to-ea-410-spring-drill-adapter/',
'https://www.ams-samplers.com/5-8threaded-male-to-ea-410-drill-adapter/',
'https://www.ams-samplers.com/3-x-6-sst-scs-complete/',
'https://www.ams-samplers.com/2-1-2-x-6-sst-scs-complete/',
'https://www.ams-samplers.com/1-1-2-x-6-sst-scs-complete/',
'https://www.ams-samplers.com/2-x-6-sst-scs-complete/',
'https://www.ams-samplers.com/2-x-4-sst-scs-complete/',
'https://www.ams-samplers.com/2-x-3-sst-scs-complete/',
'https://www.ams-samplers.com/2-x-2-sst-scs-complete/',
'https://www.ams-samplers.com/1-1-2-sst-scs-cap/',
'https://www.ams-samplers.com/3-sst-scs-cap/',
'https://www.ams-samplers.com/2-x-12-scs-cup/',
'https://www.ams-samplers.com/2-1-2-x-6-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-12-scs-complete/',
'https://www.ams-samplers.com/2-x-12-scs-cup-cap/',
'https://www.ams-samplers.com/3-x-6-scs-cup-cap/',
'https://www.ams-samplers.com/3-scs-cap/',
'https://www.ams-samplers.com/3-x-6-scs-cup/',
'https://www.ams-samplers.com/3-x-6-scs-complete/',
'https://www.ams-samplers.com/2-1-2-x-6-scs-complete/',
'https://www.ams-samplers.com/2-1-2-scs-cap/',
'https://www.ams-samplers.com/2-1-2-x-6-scs-cup/',
'https://www.ams-samplers.com/1-1-2-scs-cap/',
'https://www.ams-samplers.com/1-1-2-x-6-scs-cup/',
'https://www.ams-samplers.com/1-1-2-x-6-scs-complete/',
'https://www.ams-samplers.com/1-1-2-x-6-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-8-scs-cup/',
'https://www.ams-samplers.com/2-hex-quick-pin-core-sampler-cap/',
'https://www.ams-samplers.com/2-x-6-scs-cup/',
'https://www.ams-samplers.com/2-x-4-scs-cup/',
'https://www.ams-samplers.com/2-x-3-scs-cup/',
'https://www.ams-samplers.com/2-x-2-scs-cup/',
'https://www.ams-samplers.com/2-x-6-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-4-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-3-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-2-scs-cup-cap/',
'https://www.ams-samplers.com/2-x-6-soil-core-sampler-complete/',
'https://www.ams-samplers.com/2-x-4-scs-complete/',
'https://www.ams-samplers.com/2-x-3-scs-complete/',
'https://www.ams-samplers.com/2-x-2-scs-complete/',
'https://www.ams-samplers.com/1-1-2-x-12-scs-cup/',
'https://www.ams-samplers.com/1-1-2-x-12-scs-complete/',
'https://www.ams-samplers.com/1-1-2-x-12-scs-cup-cap/',
'https://www.ams-samplers.com/3-signature-scs-cap/',
'https://www.ams-samplers.com/3-hex-qp-scs-cap/',
'https://www.ams-samplers.com/2-1-2-scs-cap-w-3-4-threads/',
'https://www.ams-samplers.com/1-1-2-hex-qp-scs-cap/',
'https://www.ams-samplers.com/2-1-2-hex-qp-scs-cap/',
'https://www.ams-samplers.com/1-3-8-x-6-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-1-2-x-12-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-1-2-x-6-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-x-12-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-x-6-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-1-2-split-scs-core-tip/',
'https://www.ams-samplers.com/2-split-scs-core-tip/',
'https://www.ams-samplers.com/2-1-2-split-scs-solid-cap/',
'https://www.ams-samplers.com/2-split-scs-solid-cap/',
'https://www.ams-samplers.com/2-1-2-x-12-split-scs-cup-set/',
'https://www.ams-samplers.com/2-1-2-x-6-split-scs-cup-set/',
'https://www.ams-samplers.com/2-x-12-split-scs-cup-set/',
'https://www.ams-samplers.com/2-x-6-split-scs-cup-set/',
'https://www.ams-samplers.com/2-1-2-x-12-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-1-2-x-6-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-x-12-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-x-6-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-1-2-x-12-signature-split-scs-w-both-tips/',
'https://www.ams-samplers.com/1-3-8-x-12-signature-split-scs-w-both-tips/',
'https://www.ams-samplers.com/split-core-sampler-w-both-tips-signature-series-2-1-2-x-6/',
'https://www.ams-samplers.com/2-x-6-signature-split-scs-w-both-tips/',
'https://www.ams-samplers.com/1-3-8-x-6-signature-split-scs-w-both-tips/',
'https://www.ams-samplers.com/2-1-2-x-12-signature-split-scs-w-core-tip-signature-series/',
'https://www.ams-samplers.com/2-x-12-signature-split-scs-w-core-tip/',
'https://www.ams-samplers.com/1-3-8-x-12-signature-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-1-2-x-6-signature-split-scs-w-core-tip-signature-series/',
'https://www.ams-samplers.com/2-x-6-signature-split-scs-w-core-tip/',
'https://www.ams-samplers.com/1-3-8-x-6-signature-split-scs-w-core-tip/',
'https://www.ams-samplers.com/2-1-2-x-12-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-x-12-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/1-3-8-x-12-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-1-2-x-6-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-x-6-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/1-3-8-x-6-signature-split-scs-w-auger-tip/',
'https://www.ams-samplers.com/2-1-2-signature-split-scs-core-cap/',
'https://www.ams-samplers.com/2-signature-split-scs-core-cap/',
'https://www.ams-samplers.com/1-3-8-signature-split-scs-core-cap/',
'https://www.ams-samplers.com/2-1-2-split-scs-solid-cap-w-3-4-threads/',
'https://www.ams-samplers.com/2-hex-qp-split-core-cap/']

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

    title = soup.find("h1",class_="productView-title")
    a = (title.text.strip() if title else "not given")
    print(a)
    model = soup.find_all("dt",class_="productView-info-name")
    value = soup.find_all("dd", class_="productView-info-value")
    price = soup.find("span",class_="price price--withoutTax")
    pr = (price.text.strip() if price else "not given")
    print(pr)
    image = soup.find("img",attrs={'alt':a})
    y = (image.get("src") if image else "not given")
    print(y)

    c = (product_url)
    print(c)




    i = 0

    while i < len(model):

        j = 0

        while j < len(value):

            z = (model[i].text if model else "not given")
            print(z)

            i += 1

            x = (value[j].text if value else "not given")
            print(x)

            j += 1
            save_details: TextIO = open("ams__2RAAFG2.txt", "a+", encoding="utf-8")
            save_details.write("\n"+c+"\t"+a+"\t"+pr+"\t"+y+"\t"+"RP_"+z+"\t"+"RP_"+x)
            save_details.close()
            print("\n**Record stored into txt file.**")






 except AttributeError:

   pass

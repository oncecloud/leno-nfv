```
  api trace                                api trace [on|off][dump|save|replay <file>][status][free][post-mortem-on]
  cj                                       cj <enable | disable | dump>
  classify session                         classify session [hit-next|l2-hit-next|acl-hit-next <next_index>|policer-hit-next <policer_name>]
 table-index <nn> match [hex] [l2] [l3 ip4] [opaque-index <index>]
 [action set-ip4-fib-id <n>] [action set-ip6-fib-id <n>] [del]
  classify table                           classify table [miss-next|l2-miss_next|acl-miss-next <next_index>]
 mask <mask-value> buckets <nn> [skip <n>] [match <n>]
 [current-data-flag <n>] [current-data-offset <n>] [table <n>]
 [del] [del-chain]
  clear api histogram                      clear api histogram
  clear counters                           clear all active counters
  clear errors                             Clear error counters
  clear fib walk                           clear fib walk
  clear hardware-interfaces                Clear hardware interfaces statistics
  clear interface tag                      clear interface tag <intfc>
  clear interfaces                         Clear interfaces statistics
  clear ioam rewrite                       clear ioam rewrite
  clear ipsec counters                     clear ipsec counters
  clear l2fib                              clear l2fib
  clear node counters                      Clear node counters
  clear runtime                            Clear packet processing runtime statistics
  clear trace                              Clear trace buffer and free memory
  configure policer                        configure policer name <name> <params> 
  cop interface                            cop interface <interface-name> [disable]
  cop whitelist                            cop whitelist <interface-name> [ip4][ip6][default][fib-id <NN>][disable]
  create gre tunnel                        create gre tunnel src <addr> dst <addr> [outer-fib-id <fib>] [teb] [del]
  create host-interface                    create host-interface name <interface name> [hw-addr <mac>]
  create ipsec gre tunnel                  create ipsec gre tunnel src <addr> dst <addr> local-sa <id> remote-sa <id> [del]
  create ipsec tunnel                      create ipsec tunnel local-ip <addr> local-spi <spi> remote-ip <addr> remote-spi <spi>
  create l2tpv3 tunnel                     create l2tpv3 tunnel client <ip6> our <ip6> local-cookie <hex> remote-cookie <hex> local-session <dec> remote-session <dec>
  create loopback interface                create loopback interface [mac <mac-addr>]
  create netmap                            create netmap name [<intf name>|valeXXX:YYY] [hw-addr <mac>] [pipe] [master|slave]
  create packet-generator                  create packet-generator interface <interface name>
  create sub-interfaces                    create sub-interfaces <nn>[-<nn>] [dot1q|dot1ad|default|untagged]
  create vhost-user                        create vhost-user socket <socket-filename> [server] [feature-mask <hex>] [hwaddr <mac-addr>] [renumber <dev_instance>]
  create vxlan tunnel                      create vxlan tunnel src <local-vtep-addr> {dst <remote-vtep-addr>|group <mcast-vtep-addr> <intf-name>} vni <nn> [encap-vrf-id <nn>] [decap-next [l2|node <name>]] [del]
  create vxlan-gpe tunnel                  create vxlan-gpe tunnel local <local-addr> remote <remote-addr> vni <nn> [next-ip4][next-ip6][next-ethernet][next-nsh] [encap-vrf-id <nn>] [decap-vrf-id <nn>] [del]
  delete host-interface                    delete host-interface name <interface name>
  delete loopback interface                delete loopback interface intfc <interface>
  delete netmap                            delete netmap name <interface name>
  delete sub-interface                     delete sub-interface <interface>
  delete vhost-user                        delete vhost-user {<interface> | sw_if_index <sw_idx>}
  disable ip6 interface                    disable ip6 interface <interface>
  enable ip6 interface                     enable ip6 interface <interface>
  event-logger clear                       Clear the event log
  event-logger resize                      event-logger resize <nnn>
  event-logger restart                     Restart the event-logger
  event-logger save                        event-logger save <filename> (saves log in /tmp/<filename>)
  event-logger stop                        Stop the event-logger
  exec                                     Execute commands from file
  history                                  Show current session command history
  ikev2 profile                            ikev2 profile [add|del] <id>
ikev2 profile set <id> auth [rsa-sig|shared-key-mic] [cert-file|string|hex] <data>
ikev2 profile set <id> id <local|remote> <type> <data>
ikev2 profile set <id> traffic-selector <local|remote> ip-range <start-addr> - <end-addr> port-range <start-port> - <end-port> protocol <protocol-number>
  ip probe-neighbor                        ip probe-neighbor <interface> <ip4-addr> | <ip6-addr> [retry nn]
  ip route                                 ip route [add|del] [count <n>] <dst-ip-addr>/<width> [table <table-id>] [via <next-hop-ip-addr> [<interface>] [weight <weight>]] | [via arp <interface> <adj-hop-ip-addr>] | [via drop|punt|local<id>|arp|classify <classify-idx>] [lookup in table <out-table-id>]
  ip urpf-accept                           ip urpf-accept [table <table-id>] [add|del]
  ip virtual                               ip virtual <addr> <interface> [mac <Mi>]+
  ip6 nd                                   ip6 nd <interface> ...
  ipfix classify table                     ipfix classify table add|del <table-index>
  ipsec policy                             ipsec policy [add|del] spd <id> priority <n> 
  ipsec sa                                 ipsec sa [add|del]
  ipsec spd                                ipsec spd [add|del] <id>
  l2 rewrite entry                         l2 rewrite entry [index <index>] [mask <hex-mask>] [value <hex-value>] [skip <n_bytes>] [del]
  l2fib add                                l2fib add <mac> <bridge-domain-id> filter | <intf> [static | bvi]
  l2fib del                                l2fib del <mac> <bridge-domain-id>
  lisp adjacency                           lisp adjacency add|del vni <vni> reid <remote-eid> leid <local-eid>
  lisp eid-table map                       lisp eid-table map [del] vni <vni> vrf <vrf> | bd <bdi>
  lisp eid-table                           lisp eid-table add/del [vni <vni>] eid <eid> locator-set <locator-set> [key <secret-key> key-id sha1|sha256 ]
  lisp gpe entry                           lisp gpe entry add/del vni <vni> vrf <vrf> [leid <leid>]reid <reid> [loc-pair <lloc> <rloc> p <priority> w <weight>] [negative action <action>]
  lisp gpe iface                           lisp gpe iface add/del vni <vni> vrf <vrf>
  lisp gpe                                 lisp gpe [enable|disable]
  lisp locator-set                         lisp locator-set add/del <name> [iface <iface-name> p <priority> w <weight>]
  lisp locator                             lisp locator add/del locator-set <name> iface <iface-name> p <priority> w <weight>
  lisp map-register                        lisp map-register [enable|disable]
  lisp map-request itr-rlocs               lisp map-request itr-rlocs add/del <locator_set_name>
  lisp map-request mode                    lisp map-request mode dst-only|src-dst
  lisp map-resolver                        lisp map-resolver add/del <ip_address>
  lisp map-server                          lisp map-server add|del <ip>
  lisp pitr                                lisp pitr [disable] ls <locator-set-name>
  lisp remote-mapping                      lisp remote-mapping add|del [del-all] vni <vni> eid <est-eid> [action <no-action|natively-forward|send-map-request|drop>] rloc <dst-locator> p <prio> w <weight> [rloc <dst-locator> ... ]
  lisp rloc-probe                          lisp rloc-probe [enable|disable]
  lisp                                     lisp [enable|disable]
  loopback create-interface                loopback create-interface [mac <mac-addr>]
  loopback delete-interface                loopback delete-interface intfc <interface>
  map add domain                           map add domain ip4-pfx <ip4-pfx> ip6-pfx <ip6-pfx> ip6-src <ip6-pfx> ea-bits-len <n> psid-offset <n> psid-len <n> [map-t] [mtu <mtu>]
  map add rule                             map add rule index <domain> psid <psid> ip6-dst <ip6-addr>
  map del domain                           map del domain index <domain>
  map params fragment ignore-df            map params fragment ignore-df on|off
  map params fragment                      map params fragment inner|outer
  map params icmp source-address           map params icmp source-address <ip4-address>
  map params icmp6 unreachables            map params icmp6 unreachables {on|off}
  map params pre-resolve                    map params pre-resolve {ip4-nh <address>} | {ip6-nh <address>}
  map params reassembly                    map params reassembly [ip4 | ip6] [lifetime <lifetime-ms>] [pool-size <pool-size>] [buffers <buffers>] [ht-ratio <ht-ratio>]
  map params security-check fragments      map params security-check fragments on|off
  map params security-check                map params security-check on|off
  map params traffic-class                 map params traffic-class {0x0-0xff | copy}
  memory-trace                             Enable/disable memory allocation trace
  mpls local-label                         Create/Delete MPL local labels
  mpls tunnel                              mpls tunnel via [addr] [interface] [out-labels]
  oam                                      oam [add|del] target <ip4-address> fib <fib-id>
  packet-generator capture                 packet-generator capture <interface name> pcap <filename> [count <n>]
  packet-generator configure               Change packet generator stream parameters
  packet-generator delete                  Delete stream with given name
  packet-generator disable-stream          Disable packet generator streams
  packet-generator enable-stream           Enable packet generator streams
  packet-generator new                     Create packet generator stream
  pcap drop trace                          pcap drop trace on off max <nn> intfc <intfc> file <name> status
  pcap tx trace                            pcap tx trace on off max <nn> intfc <intfc> file <name> status
  ping                                     ping {<ip-addr> | ipv4 <ip4-addr> | ipv6 <ip6-addr>} [ipv4 <ip4-addr> | ipv6 <ip6-addr>] [source <interface>] [size <pktsize>] [interval <sec>] [repeat <cnt>] [table-id <id>] [verbose]
  quit                                     Exit CLI
  renumber interface                       renumber interface <if-name> <new-dev-instance>
  set affinity                             Set process cpu affinity
  set api-trace                            API trace
  set bridge-domain arp entry              set bridge-domain arp entry <bridge-domain-id> <ip-addr> <mac-addr> [del]
  set bridge-domain arp term               set bridge-domain arp term <bridge-domain-id> [disable]
  set bridge-domain flood                  set bridge-domain flood <bridge-domain-id> [disable]
  set bridge-domain forward                set bridge-domain forward <bridge-domain-id> [disable]
  set bridge-domain learn                  set bridge-domain learn <bridge-domain-id> [disable]
  set bridge-domain mac-age                set bridge-domain mac-age <bridge-domain-id> <mins>
  set bridge-domain rewrite                set bridge-domain rewrite <bridge-domain> [disable]
  set bridge-domain uu-flood               set bridge-domain uu-flood <bridge-domain-id> [disable]
  set dhcp client                          set dhcp client [del] intfc <interface> [hostname <name>]
  set dhcp option-82 vss                   set dhcp option-82 vss [del] table <table id> oui <oui> vpn-id <vpn-id>
  set dhcp proxy                           set dhcp proxy [del] server <ip-addr> src-address <ip-addr> [add-option-82] [server-fib-id <n>] [rx-fib-id <n>]
  set dhcpv6 proxy                         set dhcpv6 proxy [del] server <ipv6-addr> src-address <ipv6-addr> [add-vss-option] [server-fib-id <fib-id>] [rx-fib-id <fib-id>] 
  set dhcpv6 vss                           set dhcpv6 vss table <table-id> oui <oui> vpn-idx <vpn-idx>
  set dpdk interface descriptors           set dpdk interface descriptors <if-name> [rx <n>] [tx <n>]
  set dpdk interface hqos pipe             set dpdk interface hqos pipe <if-name> subport <n> pipe <n> profile <n>
  set dpdk interface hqos pktfield         set dpdk interface hqos pktfield <if-name> id <n> offset <n> mask <n>
  set dpdk interface hqos placement        set dpdk interface hqos placement <if-name> thread <n>
  set dpdk interface hqos subport          set dpdk interface hqos subport <if-name> subport <n> [rate <n>] [bktsize <n>] [tc0 <n>] [tc1 <n>] [tc2 <n>] [tc3 <n>] [period <n>]
  set dpdk interface hqos tctbl            set dpdk interface hqos tctbl <if-name> entry <n> tc <n> queue <n>
  set dpdk interface placement             set dpdk interface placement <if-name> [queue <n>]  thread <n>
  set fib walk histogram elements size     set fib walk histogram elements size
  set fib walk quota                       set fib walk quota
  set flow classify                        set flow classify interface <int> [ip4-table <index>]
  [ip6-table <index>] [del]
  set ikev2 local key                      set ikev2 local key <file>
  set interface feature                    set interface feature <intfc> <feature_name> arc <arc_name>
  set interface handoff                    set interface handoff <interface-name> workers <workers-list> [symmetrical|asymmetrical]
  set interface hw-class                   Set interface hardware class
  set interface input acl                  set interface input acl intfc <int> [ip4-table <index>]
  [ip6-table <index>] [l2-table <index>] [del]
  set interface ip address                 set interface ip address <interface> [<ip-addr>/<mask> [del]] | [del all]
  set interface ip source-and-port-range-c set interface ip source-and-port-range-check <interface> [tcp-out-vrf <table-id>] [udp-out-vrf <table-id>] [tcp-in-vrf <table-id>] [udp-in-vrf <table-id>] [del]
  set interface ip source-check            set interface ip source-check <interface> [strict|loose] [del]
  set interface ip table                   set interface ip table <interface> <table-id>
  set interface ip vxlan-bypass            set interface ip vxlan-bypass <interface> [del]
  set interface ip6 l2tpv3                 set interface ip6 l2tpv3 <intfc> [del]
  set interface ip6 table                  set interface ip6 table <interface> <table-id>
  set interface ipsec key                  set interface ipsec key <int> <local|remote> <crypto|integ> <key type> <key>
  set interface ipsec spd                  set interface ipsec spd <int> <id>
  set interface l2 bridge                  set interface l2 bridge <interface> <bridge-domain-id> [bvi] [shg]
  set interface l2 efp-filter              set interface l2 efp-filter <interface> [disable]
  set interface l2 flood                   set interface l2 flood <interface> [disable]
  set interface l2 forward                 set interface l2 forward <interface> [disable]
  set interface l2 input classify          set interface l2 input classify intfc <interface-name> [ip4-table <n>]
  [ip6-table <n>] [other-table <n>]
  set interface l2 learn                   set interface l2 learn <interface> [disable]
  set interface l2 output classify         set interface l2 output classify intfc <<interface-name>> [ip4-table <n>]
  [ip6-table <n>] [other-table <n>]
  set interface l2 pbb-tag-rewrite         set interface l2 pbb-tag-rewrite <interface> [disable | pop | push | translate_pbb_stag <outer_tag> dmac <address> smac <address> s_id <nn> [b_vlanid <nn>]]
  set interface l2 rewrite                 set interface l2 rewrite <interface> [table <table index>] [miss-index <entry-index>]
  set interface l2 tag-rewrite             set interface l2 tag-rewrite <interface> [disable | pop {1|2} | push {dot1q|dot1ad} <tag> <tag>]
  set interface l2 xconnect                set interface l2 xconnect <interface> <peer interface>
  set interface l2 xcrw                    set interface l2 xcrw <interface> next <node-name>
    [del] [tx-fib-id <id>] [ipv6] rw <hex-bytes>
  set interface l3                         set interface l3 <interface>
  set interface lldp                       set interface lldp <interface> (enable | disable) 
  set interface mac address                set interface mac address <intfc> <mac-address>
  set interface mpls                       Enable/Disable an interface for MPLS forwarding
  set interface mtu                        set interface mtu <value> <intfc>
  set interface promiscuous                set interface promiscuous [on | off] <intfc>
  set interface proxy-arp                  set interface proxy-arp <intfc> [enable|disable]
  set interface span                       set interface span <if-name> [disable | destination <if-name> [both|rx|tx]]
  set interface state                      Set interface state
  set interface tag                        set interface tag <intfc> <tag>
  set interface unnumbered                 set interface unnumbered [<intfc> use <intfc> | del <intfc>]
  set ioam rewrite                         set ioam [trace] [pot] [seqno] [analyse]
  set ip arp                               set ip arp [del] <intfc> <ip-address> <mac-address> [static] [count <count>] [fib-id <fib-id>] [proxy <lo-addr> - <hi-addr>]
  set ip classify                          set ip classify intfc <interface> table-index <classify-idx>
  set ip flow-hash                         set ip flow-hash table <table-id> [src] [dst] [sport] [dport] [proto] [reverse]
  set ip source-and-port-range-check       set ip source-and-port-range-check vrf <table-id> <ip-addr>/<mask> {port nn | range <nn> - <nn>} [del]
  set ip6 classify                         set ip6 classify intfc <interface> table-index <classify-idx>
  set ip6 flow-hash                        set ip6 flow-hash table <table-id> [src] [dst] [sport] [dport] [proto] [reverse]
  set ip6 link-local address               set ip6 link-local address <interface> <ip6-address>/<width>
  set ip6 neighbor                         set ip6 neighbor [del] <interface> <ip6-address> <mac-address> [static]
  set ip6 sr rewrite                       set ip6 sr rewrite <ip6-address> [fib-id <id>]
  set ipfix classify stream                set ipfix classify stream[domain <domain-id>] [src-port <src-port>]
  set ipfix exporter                       set ipfix exporter collector <ip4-address> [port <port>] src <ip4-address> [fib-id <fib-id>] [path-mtu <path-mtu>] [template-interval <template-interval>]
  set ipsec sa                             set ipsec sa <id> crypto-key <key> integ-key <key>
  set l2tpv3 tunnel cookie                 set l2tpv3 tunnel cookie <intfc> local <hex> remote <hex>
  set li                                   set li src <ip4-address> collector <ip4-address> udp-port <nnnn>
  set lldp                                 set lldp [system-name <string>] [tx-hold <value>] [tx-interval <value>]
  set policer classify                     set policer classify interface <int> [ip4-table <index>]
  [ip6-table <index>] [l2-table <index>] [del]
  set punt udp                             set punt udp [del] <all | port-num1 [port-num2 ...]>
  set significant error                    set significant error <counter-index-nnn> [disable]
  set terminal ansi                        set terminal ansi [on|off]
  set terminal history                     set terminal history [on|off] [limit <lines>]
  set terminal pager                       set terminal pager [on|off] [limit <lines>]
  show adj nbr                             show adj nbr [<adj_index>] [interface]
  show adj                                 show adj [<adj_index>] [interface]
  show affinity                            Show process cpu affinity
  show api clients                         Client information
  show api histogram                       show api histogram
  show api message-table                   Message Table
  show api plugin                          show api plugin
  show api ring-stats                      Message ring statistics
  show api status                          Show API trace status
  show arp-nd-event registrations          Show ip4 arp and ip6 nd event registrations
  show bridge-domain                       show bridge-domain [bridge-domain-id [detail|int|arp]]
  show buffers                             Show packet buffer allocation
  show cdp                                 Show cdp command
  show classify flow                       show classify flow type [ip4|ip6]
  show classify policer                    show classify policer type [ip4|ip6|l2]
  show classify tables                     show classify tables [index <nn>]
  show cpu                                 Show cpu information
  show dhcp client                         show dhcp client [intfc <intfc>][verbose]
  show dhcp option-82-address interface    show dhcp option-82-address interface <interface>
  show dhcp proxy                          Display dhcp proxy server info
  show dhcp vss                            show dhcp VSS
  show dhcpv6 link-address interface       show dhcpv6 link-address interface <interface>
  show dhcpv6 proxy                        Display dhcpv6 proxy info
  show dhcpv6 vss                          show dhcpv6 VSS
  show dpdk buffer                         show dpdk buffer state
  show dpdk hqos queue                     show dpdk hqos queue <if-name> subport <subport> pipe <pipe> tc <tc> tc_q <tc_q>
  show dpdk interface hqos placement       show dpdk interface hqos placement
  show dpdk interface hqos                 show dpdk interface hqos <if-name>
  show dpdk interface placement            show dpdk interface placement
  show dpo memory                          show dpo memory
  show errors                              Show error counts
  show event-logger                        Show event logger info
  show features                            show features
  show fib entry                           show fib entry
  show fib memory                          show fib memory
  show fib path-lists                      show fib path-lists
  show fib paths                           show fib paths
  show fib uRPF                            show fib uRPF
  show fib walk                            show fib walk
  show frame-queue histogram               show frame-queue histogram
  show frame-queue                         show frame-queue trace
  show gdb                                 Describe functions which can be called from gdb
  show gre tunnel                          show gre tunnel commands
  show hardware-interfaces                 show hardware-interfaces [brief|verbose|detail] [bond] [<if-name1> <if-name2> ...]
  show ikev2 profile                       show ikev2 profile
  show ikev2 sa                            show ikev2 sa
  show inacl                               show inacl type [ip4|ip6|l2]
  show interfaces span                     Shows SPAN mirror table
  show interfaces                          show interfaces [address|addr|features|feat] [<if-name1> <if-name2> ...]
  show ioam summary                        show ioam summary
  show ip arp                              show ip arp
  show ip fib                              show ip fib [summary] [table <table-id>] [index <fib-id>] [<ip4-addr>[/<mask>]] [mtrie]
  show ip local                            show ip local
  show ip source-and-port-range-check      show ip source-and-port-range-check vrf <table-id> <ip-addr> [port <n>]
  show ip6 fib                             show ip6 fib [summary] [table <table-id>] [index <fib-id>] [<ip6-addr>[/<width>]]
  show ip6 interface                       show ip6 interface <interface>
  show ip6 local                           show ip6 local
  show ip6 neighbors                       show ip6 neighbors [<interface>]
  show ipsec gre tunnel                    show ipsec gre tunnel commands
  show ipsec                               show ipsec
  show l2 rewrite entries                  show l2 rewrite entries
  show l2 rewrite interfaces               show l2 rewrite interfaces
  show l2fib                               show l2fib [verbose | bd_id <nn> | bd_index <nn> | raw]
  show l2patch                             Show l2 interface cross-connect entries
  show l2tpv3                              show l2tpv3 [verbose]
  show l2xcrw                              show l2xcrw
  show lisp adjacencies                    show lisp adjacencies
  show lisp eid-table map                  show lisp eid-table l2|l3
  show lisp eid-table                      Shows EID table
  show lisp gpe adjacency                  show lisp gpe adjacency commands
  show lisp gpe entry                      show lisp gpe entry vni <vni> vrf <vrf> [leid <leid>] reid <reid>
  show lisp gpe interface                  show lisp gpe interface
  show lisp gpe sub-interface              show lisp gpe sub-interface
  show lisp gpe tenant                     show lisp gpe tenant
  show lisp gpe tunnel                     show lisp gpe tunnel commands
  show lisp locator-set                    Shows locator-sets
  show lisp map-request itr-rlocs          Shows map-request itr-rlocs
  show lisp map-request mode               show lisp map-request mode
  show lisp map-resolvers                  show lisp map-resolvers
  show lisp pitr                           Show pitr
  show lisp status                         show lisp status
  show lldp                                show lldp [detail]
  show load-balance                        show load-balance [<index>]
  show load-balance-map                    show load-balance-map [<index>]
  show map domain                          show map domain index <n> [counters]
  show map fragments                       show map fragments
  show map stats                           show map stats
  show memory                              Show current memory usage
  show mode                                show mode [<if-name1> <if-name2> ...]
  show mpls fib                            show mpls fib [summary] [table <n>]
  show mpls tunnel                         show mpls tunnel commands
  show node counters                       Show node counters
  show oam                                 show oam
  show packet-generator                    Show packet generator streams
  show pci                                 show pci [all]
  show physmem                             Show physical memory allocation
  show plugins                             show loaded plugins
  show policer                             show policer [name]
  show runtime                             Show packet processing runtime
  show sr hmac                             show sr hmac
  show sr multicast-map                    show sr multicast-map
  show sr policy                           show sr policy [name <sr-policy-name>]
  show sr tunnel                           show sr tunnel [name <sr-tunnel-name>]
  show terminal                            Show current session terminal settings
  show threads                             Show threads
  show trace                               Show trace buffer [max COUNT]
  show unix-errors                         Show Unix system call error history
  show version                             show version information
  show vhost-user                          show vhost-user [<interface> [<interface> [..]]] [descriptors]
  show vlib frame-allocation               Show node dispatch frame statistics
  show vlib graph                          Show packet processing node graph
  show vxlan tunnel                        show vxlan tunnel
  show vxlan-gpe                           show vxlan-gpe commands
  sr hmac                                  sr hmac [del] id <nn> key <str>
  sr multicast-map                         sr multicast-map address <multicast-ip6-address> sr-policy <sr-policy-name> [del]
  sr policy                                sr policy [del] name <policy-name> tunnel <sr-tunnel-name> [tunnel <sr-tunnel-name>]*
  sr tunnel                                sr tunnel [del] [name <name>] src <addr> dst <addr> [next <addr>] [clean] [reroute] [key <secret>] [policy <policy_name>][rx-fib-id <fib_id>] [tx-fib-id <fib_id>]
  tap connect                              tap connect <intfc-name> [hwaddr <addr>]
  tap delete                               tap delete <vpp-tap-intfc-name>
  tap modify                               tap modify <vpp-tap-intfc-name> <linux-intfc-name> [hwaddr <addr>]
  test classify                            test classify [src <ip>] [sessions <nn>] [buckets <nn>] [table <nn>] [del]
  test counters                            increment all active counters
  test dpdk buffer                         test dpdk buffer [allocate <nn>][free <nn>]
  test fib                                 fib unit tests - DO NOT RUN ON A LIVE SYSTEM
  test frame-queue nelts                   test frame-queue nelts (4,8,16,32)
  test frame-queue threshold               test frame-queue threshold N (0=no limit)
  test heap-validate                       <on/off/now> validate heap on future allocs/frees or right now
  test ip6 link                            test ip6 link <mac-address>
  test l2fib                               test l2fib [add|del|check] mac <base-addr> count <nn>
  test l2patch                             test l2patch rx <intfc> tx <intfc> [del]
  test lookup                              test lookup <ipv4-addr> [table <fib-id>] [count <nn>]
  test policer                             intfc <intfc> policer <policer-config-name> [del]
  test sr debug                            test sr debug on|off
  test sr hmac                             test sr hmac validate [on|off]
  trace add                                Trace given number of packets
  trace filter                             filter trace output - include NODE COUNT | exclude NODE COUNT | none
  trace frame-queue                        trace frame-queue (on|off)
  vhost thread                             vhost thread <iface> <worker-index> [del]
```

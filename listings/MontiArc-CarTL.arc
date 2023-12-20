component CarTL {
  // Define ports
  port <<sync>> out Signal signal;
  // Define behavior as automaton
  automaton {
    initial state Red;
    state RedAmber;
    state Green;
    state Amber;
    // Define transitions sending events
    Red -> RedAmber;
    RedAmber -> Green / {
      signal = Signal.RED;
    };
    Green -> Amber;
    Amber -> Red / {
      signal = Signal.GREEN;
    };
  }
}
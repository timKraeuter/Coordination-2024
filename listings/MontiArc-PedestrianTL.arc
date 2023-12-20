component PedestrianTL {
  port <<sync>> out Signal signal;

  automaton {
    initial state Red;
    state RedAmber;
    state Green;
    state Amber;

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
component PedestrianCrossing {
  // Define subcomponents
  CarTL ctl;
  PedestrianTL ptl;
  // Define connectors
  ctl.signal -> ptl.signal;
}
component CarTL {
  // Define ports
  port <<sync>> out Signal signal;
  ...
}
component PedestrianTL {
  // Define ports
  port <<sync>> in Signal signal;
  ...
}
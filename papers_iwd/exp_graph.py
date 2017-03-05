import matplotlib.pyplot as plt
x = range(1,16)
y = [[0.95, 0.0475, 0.0023750000000000004, 0.00011875000000000003, 5.937500000000001e-06, 2.9687500000000007e-07, 1.4843750000000005e-08, 7.421875000000002e-10, 3.7109375000000016e-11, 1.855468750000001e-12, 9.277343750000005e-14, 4.638671875000002e-15, 2.3193359375000015e-16, 1.1596679687500008e-17, 5.798339843750004e-19], [0.7800000001067665, 0.17160000002348863, 0.0377520000051675, 0.00830544000113685, 0.001827196800250107, 0.00040198329605502345, 8.843632513210518e-05, 1.945599152906314e-05, 4.28031813639389e-06, 9.41669990006656e-07, 2.071673978014643e-07, 4.557682751632215e-08, 1.0026902053590873e-08, 2.2059184517899916e-09, 4.853020593937983e-10], [0.5800012946975286, 0.243600543772962, 0.10231222838464404, 0.04297113592155049, 0.018047877087051207, 0.007580108376561507, 0.003183645518155833, 0.0013371311176254498, 0.0005615950694026889, 0.00023586992914912931, 9.906537024263431e-05, 4.160745550190641e-05, 1.747513131080069e-05, 7.33955515053629e-06, 3.082613163225242e-06], [0.3802924105251712, 0.23578129452560614, 0.1461844026058758, 0.090634329615643, 0.05619328436169865, 0.03483983630425317, 0.021600698508636964, 0.013392433075354915, 0.008303308506720048, 0.00514805127416643, 0.0031917917899831863, 0.0019789109097895757, 0.001226924764069537, 0.000760693353723113, 0.00047162987930832997], [0.18966483873393147, 0.1555251677618238, 0.1275306375646955, 0.1045751228030503, 0.08575160069850124, 0.07031631257277102, 0.05765937630967223, 0.04728068857393122, 0.038770164630623605, 0.03179153499711135, 0.02606905869763131, 0.02137662813205767, 0.01752883506828729, 0.014373644755995577, 0.011786388699916373], [0.0714583566197687, 0.070743773053571, 0.07003633532303528, 0.06933597196980494, 0.06864261225010689, 0.06795618612760582, 0.06727662426632977, 0.06660385802366646, 0.0659378194434298, 0.0652784412489955, 0.06462565683650554, 0.06397940026814049, 0.06333960626545908, 0.06270621020280448, 0.06207914810077644]]

plt.plot(x,y[0],linestyle='-', marker='o', label='SP = 0.02')
plt.plot(x,y[1],linestyle='-', marker='^', label='SP = 0.22')
plt.plot(x,y[2],linestyle='-', marker='s', label='SP = 0.42')
plt.plot(x,y[3],linestyle='-', marker='p', label='SP = 0.62')
plt.plot(x,y[4],linestyle='-', marker='h', label='SP = 0.82')
plt.plot(x,y[5],linestyle='-', marker='D', label='SP = 0.99')

plt.title('Exponential ranking selection')
plt.xlabel('Individuals rank')
plt.ylabel('Selection probability value')
plt.axis([0, len(x)+1, 0, 1.0])
plt.grid(True)
plt.legend()

plt.show()

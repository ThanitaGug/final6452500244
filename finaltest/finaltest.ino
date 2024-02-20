#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;

std_msgs::Int16 sensorData1;
ros::Publisher pub1("Topic_s1", &sensorData1);
std_msgs::Int16 sensorData2;
ros::Publisher pub2("Topic_s2", &sensorData2);
std_msgs::Int16 sensorData3;
ros::Publisher pub3("Topic_s3", &sensorData3);
std_msgs::Int16 sensorData0;
ros::Publisher pub0("Topic_s0", &sensorData0);



void control_LED( const std_msgs::Int16& cmd_msg){
  int value = cmd_msg.data;
  digitalWrite(13, value );   // blink the led
}
ros::Subscriber<std_msgs::Int16> sub ("Topic_led", &control_LED );

void setup() {
  pinMode(13, OUTPUT); ///led
  pinMode(1, INPUT);  //SW
  pinMode(2, INPUT);  //SW
  pinMode(3, INPUT);  //SW
  nh.initNode();
  nh.subscribe(sub); ///สำคัญ
  nh.advertise(pub1);
  nh.advertise(pub2);
  nh.advertise(pub3);
  nh.advertise(pub0);

}
int sensordata = 0;
void loop() {
  if (digitalRead(1)==1){
    if (sensordata == 0){
      sensordata = sensordata+1;
      pub0.publish(sensordata);
    }
    else{
      sensordata = sensordata-1;
      pub1.publish(sensordata);
    }
  }
  else if(digitalRead(2)==1){
    sensorData2.data = digitalRead(2);
    pub2.publish(2);
  }
  else if(digitalRead(3)==1){
    sensorData3.data = digitalRead(3);
    pub3.publish(3);
  }
  nh.spinOnce();
  delay(100);
}

#include <math.h>
#include <functional>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <ignition/math/Vector3.hh>
#include <ignition/math/Pose3.hh>
//#include <gazebo/common/State.hh>

namespace gazebo
{
  class ModelPush : public ModelPlugin
  {
    public: void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
      // Store the pointer to the model
      this->model = _parent;
      //this->world = this->model->GetWorld();

      // Listen to the update event. This event is broadcast every
      // simulation iteration.
      this->updateConnection = event::Events::ConnectWorldUpdateBegin(
          std::bind(&ModelPush::OnUpdate, this));
    }

    // Called by the world update start event
    public: void OnUpdate()
    {
      // Apply a small linear velocity to the model.
      //this->model->GetChildLink("link")->AddForce(ignition::math::Vector3d(0,10,0));
      //this->model->SetLinearVel(ignition::math::Vector3d(.3, 0, 0));
      double time =  this->model->GetWorld()->SimTime().Double();
      double yVel = this->model->WorldLinearVel().X();
      double xVel = this->model->WorldLinearVel().Y();

      double omega = 5.0;

      double force = 1.0 * sin(omega*time);
      //this->model->GetChildLink("link")->AddForce(ignition::math::Vector3d(0,force,0));
      this->model->SetLinearVel(ignition::math::Vector3d(0, force, 0));
      printf("%lf\n",this->model->WorldPose().CoordPositionAdd(ignition::math::Vector3d(0,0,0)).Y());
    }

    // Pointer to the model
    private: physics::ModelPtr model;

    // Pointer to the update event connection
    private: event::ConnectionPtr updateConnection;
    //private: physics::WorldPtr world;
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(ModelPush)
}

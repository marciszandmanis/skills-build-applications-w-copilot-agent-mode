from rest_framework import serializers
from .models import CustomUser, Team, Activity, Workout, Leaderboard
from bson import ObjectId

# Helper to convert ObjectId to string
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'distance']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points']

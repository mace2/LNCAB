from rest_framework import serializers
from tournaments.models import Game


class GameSerializer(serializers.ModelSerializer):
    team_local = serializers.SlugRelatedField(read_only=True, slug_field="name")
    team_visitor = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Game
        fields = ('id', 'team_local', 'team_visitor','local_points','visitor_points',
                  'local_q1','local_q2','local_q3','local_q4','visitor_q1','visitor_q2',
                  'visitor_q3','visitor_q4','local_points','visitor_points')

    def update(self, instance, validated_data):
        print(validated_data)
        return instance
